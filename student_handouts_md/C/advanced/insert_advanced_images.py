from pathlib import Path
import shutil

BASE = Path(__file__).resolve().parent

SPECS = {
    "01_進階指標.md": [
        ("## Section IV. 一般陣列與指標陣列",
         "C_Advanced_01_img01_pointer_array.png",
         "指標陣列的記憶體結構"),

        ("## Section IX. 完整陣列也有位址",
         "C_Advanced_01_img02_pointer_array_vs_array_pointer.png",
         "指標陣列與陣列指標的差異"),

        ("### 12. 宣告陣列指標",
         "C_Advanced_01_img03_array_pointer_memory.png",
         "陣列指標與完整陣列的記憶體關係"),

        ("### 14. 為什麼需要括號？",
         "C_Advanced_01_img04_parentheses_precedence.png",
         "指標宣告中括號與下標的優先順序"),

        ("## Section XIII. 二維陣列是陣列的陣列",
         "C_Advanced_01_img05_real_2d_array.png",
         "真正二維陣列的記憶體配置"),

        ("# Part E：為什麼真正二維陣列不是 `int **`",
         "C_Advanced_01_img06_2d_array_vs_double_pointer.png",
         "真正二維陣列與雙重指標的差異"),

        ("### 26. 可以重新排列列順序",
         "C_Advanced_01_img07_row_pointer_reorder.png",
         "利用列指標重新排列二維資料"),

        ("### 29. 索引推導",
         "C_Advanced_01_img08_flattened_index.png",
         "二維資料扁平化索引"),

        ("## Section XXIII. 兩種方法比較",
         "C_Advanced_01_img09_2d_char_vs_string_pointers.png",
         "二維字元陣列與字串指標陣列比較"),

        ("### 45. 記憶體圖",
         "C_Advanced_01_img10_compact_string_storage.png",
         "緊密字串儲存的記憶體配置"),

        ("# Part G：傳遞任意長寬二維資料",
         "C_Advanced_01_img11_2d_parameter_methods.png",
         "三種二維資料參數介面"),

        ("## Section XXXIX. 緊密儲存需要兩種容量檢查",
         "C_Advanced_01_img12_compact_storage_capacity.png",
         "緊密字串儲存的容量檢查流程"),
    ],

    "02_指標陣列與陣列指標.md": [
        ("## Section III. 核心宣告對照",
         "C_Advanced_02_img01_pointer_array_vs_array_pointer.png",
         "指標陣列與陣列指標總覽"),

        ("## Section V. 指標陣列指向同一陣列的元素",
         "C_Advanced_02_img02_pointer_array_mapping.png",
         "指標陣列與原陣列元素的對應"),

        ("### 8. 使用兩個下標",
         "C_Advanced_02_img03_double_subscript.png",
         "雙下標操作的解析流程"),

        ("## Section VIII. 每一列可以有不同長度",
         "C_Advanced_02_img04_jagged_rows.png",
         "不等長列的指標陣列"),

        ("## Section IX. 完整陣列也有位址",
         "C_Advanced_02_img05_address_of_array.png",
         "陣列位址與陣列指標"),

        ("### 14. 為什麼需要括號？",
         "C_Advanced_02_img06_declaration_parentheses.png",
         "括號如何改變指標宣告"),

        ("### 17. 固定長度成為型態的一部分",
         "C_Advanced_02_img07_pointer_stride.png",
         "不同陣列指標型態的移動距離"),

        ("## Section XIII. 二維陣列是陣列的陣列",
         "C_Advanced_02_img08_real_2d_array.png",
         "真正二維陣列的記憶體配置"),

        ("# Part E：為什麼真正二維陣列不是 `int **`",
         "C_Advanced_02_img09_2d_array_vs_double_pointer.png",
         "真正二維陣列與雙重指標比較"),

        ("# Part G：傳遞任意長寬二維資料",
         "C_Advanced_02_img10_2d_interfaces.png",
         "三種二維資料介面比較"),

        ("## Section XV. 三種相關位址",
         "C_Advanced_02_img11_same_address_different_type.png",
         "相同位址數值但不同指標型態"),

        ("### 26. 可以重新排列列順序",
         "C_Advanced_02_img12_reorder_row_pointers.png",
         "重新排列列指標而不搬動資料"),

        ("### 29. 索引推導",
         "C_Advanced_02_img13_flattened_index.png",
         "二維資料扁平化索引公式"),

        ("# Part H：常見宣告閱讀法",
         "C_Advanced_02_img14_declaration_reading.png",
         "常見複雜指標宣告閱讀法"),
    ],

    "03_指標轉型.md": [
        ("## Section III. 轉型總覽",
         "C_Advanced_03_img01_pointer_conversion_overview.png",
         "C 指標轉型總覽"),

        ("## Section IV.",
         "C_Advanced_03_img02_array_pointer_types.png",
         "不同陣列長度對應不同指標型態"),

        ("## Section VI.",
         "C_Advanced_03_img03_double_pointer_vs_array_pointer.png",
         "雙重指標與陣列指標比較"),

        ("## Section X.",
         "C_Advanced_03_img04_const_pointer_conversion.png",
         "增加 const 與移除 const 的差異"),

        ("## Section XII.",
         "C_Advanced_03_img05_void_pointer_round_trip.png",
         "void 指標往返原型態"),

        ("## Section XVII.",
         "C_Advanced_03_img06_pointer_integer_conversion.png",
         "指標與整數之間的轉換"),

        ("### 22. 強制轉型不會做什麼？",
         "C_Advanced_03_img07_cast_does_not_change_object.png",
         "強制轉型不會改變原物件"),

        ("## Section XIX.",
         "C_Advanced_03_img08_memory_alignment.png",
         "指標轉型與記憶體對齊"),

        ("## Section XXII.",
         "C_Advanced_03_img09_cast_roundtrip_dereference.png",
         "可以轉型不代表可以安全解參照"),

        ("## Section XXIII.",
         "C_Advanced_03_img10_object_bytes_endianness.png",
         "使用 unsigned char 觀察物件位元組與端序"),
    ],

    "04_函式指標.md": [
        ("## Section III. 核心宣告對照",
         "C_Advanced_04_img01_function_vs_function_pointer.png",
         "一般函式與函式指標"),

        ("### 3. 為什麼需要括號？",
         "C_Advanced_04_img02_parentheses_change_meaning.png",
         "函式指標宣告中括號的重要性"),

        ("## Section IX. 讓函式指標指向函式",
         "C_Advanced_04_img03_function_designator_to_pointer.png",
         "函式名稱轉換為函式指標"),

        ("## Section XI. 簡化呼叫方式",
         "C_Advanced_04_img04_function_pointer_call.png",
         "函式指標的兩種呼叫方式"),

        ("## Section XVIII. 使用標準函式觀察規則",
         "C_Advanced_04_img05_printf_pointer_relationship.png",
         "printf 與函式指標的關係"),

        ("## Section XXII. 對應的函式指標型態",
         "C_Advanced_04_img06_read_function_pointer_declaration.png",
         "函式指標宣告閱讀方式"),

        ("## Section XXIV. 改指向 multiply()",
         "C_Advanced_04_img07_switch_function_target.png",
         "同一函式指標切換不同函式"),

        ("## Section XXV. 必須比較哪些部分？",
         "C_Advanced_04_img08_function_pointer_compatibility.png",
         "函式指標型態相容性"),

        ("## Section XXXIII. 這就是 callback",
         "C_Advanced_04_img09_callback_flow.png",
         "函式指標 callback 的資料與呼叫流程"),

        ("## Section XXXVIII. 宣告函式指標陣列",
         "C_Advanced_04_img10_function_pointer_array.png",
         "函式指標陣列"),

        ("## Section XXXV. 使用 typedef",
         "C_Advanced_04_img11_typedef_function_pointer.png",
         "使用 typedef 簡化函式指標型態"),

        ("## Section L. hello 與 hello()",
         "C_Advanced_04_img12_function_vs_function_call.png",
         "函式本身與立即呼叫函式的差異"),
    ],
}


def image_block(image, alt):
    return (
        '\n'
        '<p align="center">\n'
        '  <img\n'
        f'    src="images/{image}"\n'
        f'    alt="{alt}"\n'
        '    width="700">\n'
        '</p>\n'
    )


def find_anchor(lines, anchor):
    # First try exact line match.
    for i, line in enumerate(lines):
        if line.strip() == anchor.strip():
            return i

    # Then allow partial section matches such as "## Section IV."
    for i, line in enumerate(lines):
        if anchor.strip() in line.strip():
            return i

    return None


def main():
    inserted = 0
    skipped = 0
    missing_anchor = 0
    missing_image = 0

    for md_name, entries in SPECS.items():
        md_path = BASE / md_name

        if not md_path.exists():
            print(f"[ERROR] Markdown not found: {md_name}")
            continue

        backup = md_path.with_suffix(md_path.suffix + ".bak")

        if not backup.exists():
            shutil.copy2(md_path, backup)
            print(f"[BACKUP] {backup.name}")

        text = md_path.read_text(encoding="utf-8")

        for anchor, image, alt in entries:
            src = f'images/{image}'

            if src in text:
                print(f"[SKIP] already inserted: {image}")
                skipped += 1
                continue

            image_path = BASE / "images" / image

            if not image_path.exists():
                print(f"[IMAGE MISSING] {image}")
                missing_image += 1
                continue

            lines = text.splitlines(keepends=True)
            index = find_anchor(lines, anchor)

            if index is None:
                print(f"[ANCHOR MISSING] {md_name}: {anchor}")
                missing_anchor += 1
                continue

            block = image_block(image, alt)

            # Insert after the heading line.
            lines.insert(index + 1, block)
            text = "".join(lines)

            print(f"[INSERT] {md_name} <- {image}")
            inserted += 1

        md_path.write_text(text, encoding="utf-8")

    print()
    print("========== SUMMARY ==========")
    print(f"Inserted       : {inserted}")
    print(f"Already exists : {skipped}")
    print(f"Missing anchor : {missing_anchor}")
    print(f"Missing image  : {missing_image}")


if __name__ == "__main__":
    main()
