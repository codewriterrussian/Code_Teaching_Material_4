from __future__ import annotations

import shlex
import subprocess
from pathlib import Path

from IPython import get_ipython


BUILD_DIRECTORY = Path(".c_cpp_build")


def _parse_options(line: str, default_standard: str) -> dict:
    tokens = shlex.split(line)

    options = {
        "interactive": False,
        "input_lines": None,
        "timeout": 10.0,
        "standard": default_standard,
        "extra_flags": [],
    }

    index = 0

    while index < len(tokens):
        token = tokens[index]

        if token in {"-i", "--input"}:
            options["interactive"] = True

        elif token in {"-n", "--lines"}:
            index += 1

            if index >= len(tokens):
                raise ValueError(f"{token} requires a number.")

            options["input_lines"] = int(tokens[index])

        elif token in {"-t", "--timeout"}:
            index += 1

            if index >= len(tokens):
                raise ValueError(f"{token} requires a number.")

            options["timeout"] = float(tokens[index])

        elif token == "--std":
            index += 1

            if index >= len(tokens):
                raise ValueError("--std requires a language standard.")

            options["standard"] = tokens[index]

        else:
            # Unknown options are passed directly to clang/clang++.
            # Examples: -O2, -fsanitize=address
            options["extra_flags"].append(token)

        index += 1

    return options


def _get_program_input(
    interactive: bool,
    input_lines: int | None,
) -> str:
    if input_lines is not None:
        answers = []

        for index in range(input_lines):
            answer = input(f"Input line {index + 1}: ")
            answers.append(answer)

        return "\n".join(answers) + "\n"

    if not interactive:
        return ""

    print("Enter the program input.")
    print("Type END on a separate line when finished.")

    answers = []

    while True:
        answer = input("Input: ")

        if answer == "END":
            break

        answers.append(answer)

    if not answers:
        return ""

    return "\n".join(answers) + "\n"


def _compile_and_run_cell(
    language: str,
    line: str,
    cell: str,
) -> None:
    if language == "c":
        compiler = "clang"
        extension = ".c"
        default_standard = "c17"
    elif language == "cpp":
        compiler = "clang++"
        extension = ".cpp"
        default_standard = "c++17"
    else:
        raise ValueError(f"Unsupported language: {language}")

    try:
        options = _parse_options(line, default_standard)
    except (ValueError, TypeError) as error:
        print(f"Option error: {error}")
        return

    BUILD_DIRECTORY.mkdir(exist_ok=True)

    source_path = BUILD_DIRECTORY / f"notebook_program{extension}"
    executable_path = BUILD_DIRECTORY / f"notebook_program_{language}"

    source_path.write_text(cell, encoding="utf-8")

    compile_command = [
        compiler,
        str(source_path),
        f"-std={options['standard']}",
        "-Wall",
        "-Wextra",
        "-Wpedantic",
        "-g",
        "-O0",
        "-o",
        str(executable_path),
        *options["extra_flags"],
    ]

    compilation = subprocess.run(
        compile_command,
        text=True,
        capture_output=True,
    )

    if compilation.returncode != 0:
        print("Compilation failed:\n")

        if compilation.stdout:
            print(compilation.stdout, end="")

        if compilation.stderr:
            print(compilation.stderr, end="")

        return

    if compilation.stderr:
        print("Compiler messages:\n")
        print(compilation.stderr, end="")

    print("Compilation successful.")

    program_input = _get_program_input(
        interactive=options["interactive"],
        input_lines=options["input_lines"],
    )

    try:
        execution = subprocess.run(
            [str(executable_path)],
            input=program_input,
            text=True,
            capture_output=True,
            timeout=options["timeout"],
        )
    except subprocess.TimeoutExpired:
        print(
            f"Program stopped because it exceeded "
            f"{options['timeout']} seconds."
        )
        return
    except PermissionError:
        print(f"Permission denied: {executable_path}")
        return

    print("\nProgram output:")

    if execution.stdout:
        print(execution.stdout, end="")

    if execution.stderr:
        print("\nProgram error output:")
        print(execution.stderr, end="")

    if not execution.stdout and not execution.stderr:
        print("(No output)")

    if execution.returncode != 0:
        print(f"\nProgram exited with code {execution.returncode}.")


def _register_magics() -> None:
    ipython = get_ipython()

    if ipython is None:
        return

    def c_magic(line: str, cell: str) -> None:
        _compile_and_run_cell("c", line, cell)

    def cpp_magic(line: str, cell: str) -> None:
        _compile_and_run_cell("cpp", line, cell)

    ipython.register_magic_function(
        c_magic,
        magic_kind="cell",
        magic_name="c",
    )

    ipython.register_magic_function(
        cpp_magic,
        magic_kind="cell",
        magic_name="cpp",
    )


_register_magics()


__all__ = []