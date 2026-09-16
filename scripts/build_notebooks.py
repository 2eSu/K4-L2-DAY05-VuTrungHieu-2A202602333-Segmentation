"""Regenerate the five small, learner-facing notebooks from reviewed cells."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def md(source: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": source.splitlines(keepends=True)}


def code(source: str) -> dict:
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
            "source": source.splitlines(keepends=True)}


SETUP = '''from pathlib import Path
import sys
root = next((p for p in [Path.cwd(), *Path.cwd().parents] if (p / "data/manifest.json").is_file()), None)
assert root is not None, "Mở notebook từ thư mục repo Day 5 (hoặc thư mục notebooks/)."
sys.path.insert(0, str(root / "scripts"))
from inspect_submissions import task_registry, expected_for, inspect_task
tasks = task_registry(root)
exports = root / "submissions"
print("Repo:", root)
print("Thư mục export:", exports)
'''


NOTEBOOKS = {
    "01-bat-dau-va-nhan-anh.ipynb": [
        md("# 01 · Nhận bài và nhận ảnh\n\n**Mục tiêu:** tự kiểm đúng 9 task, 14 ảnh, tên class và trọng số trước khi vào CVAT. Notebook hỗ trợ, không phải bài nộp. Chạy từng ô bằng Shift+Enter; nếu không dùng notebook, đọc `lab-guide.html`."),
        code(SETUP),
        code('''for name, info in tasks.items():
    images, classes = expected_for(name, info, root)
    print(f"{name:18} {info['type']:9} {len(images)} ảnh · {len(classes)} class · {info['weight']} điểm")
    print("  ảnh:", ", ".join(sorted(images)))
print("Tổng điểm tối đa:", sum(info["weight"] for info in tasks.values()))
'''),
        md("## Xem một ảnh thực\n\nẢnh bên dưới là ảnh trong task, không có đường biên hay đáp án. Hãy đối chiếu tên file với CVAT khi tạo task. Đừng nộp ảnh này thay mask."),
        code('''from IPython.display import display, Image
task_name = "easy_semantic"  # đổi sang một mã task trong bảng trên nếu cần
image_file = sorted((root / "data" / tasks[task_name]["path"] / "images").glob("*.jpg"))[0]
print(task_name, image_file.name)
display(Image(filename=str(image_file), width=760))
'''),
        md("## Tự nhắc trước khi vẽ\n\n- Semantic: mỗi pixel thuộc một lớp vùng; không phải một object riêng.\n- Instance: mỗi vật đếm được là một mask riêng.\n- Panoptic: vừa stuff vừa từng thing.\n- Nếu SAM không có, dùng Brush/Polygon. Đọc `CVAT_SETUP.md`; không chờ cài tool mới được làm."),
    ],
    "02-qc-semantic.ipynb": [
        md("# 02 · QC semantic và ba checkpoint semantic\n\nXuất `Segmentation mask 1.1` từ CVAT; để ZIP vào `submissions/<mã_task>.zip`. Ô kiểm chỉ kiểm cấu trúc, ảnh và labelmap, **không so đáp án**. Không cần chạy ô này để vẽ được trên CVAT."),
        code(SETUP),
        code('''semantic_names = [name for name, info in tasks.items() if info["type"] == "semantic"]
for name in semantic_names:
    result = inspect_task(name, exports / f"{name}.zip", root)
    status = "LỖI" if result["errors"] else ("CHƯA XUẤT" if not Path(result["file"]).exists() else "OK")
    print("\\n", name, "·", status)
    print("  ảnh mask:", ", ".join(result["details"].get("mask_images", [])) or "—")
    for note in result["errors"]: print("  SỬA:", note)
    for note in result["warnings"]: print("  KIỂM:", note)
'''),
        md("## Xem mask đã export\n\nChọn đúng task và ảnh. Màu chỉ giúp nhìn vùng; mép road/sidewalk, cột mảnh và lỗ phủ vẫn phải đối chiếu ảnh gốc bằng mắt. Nếu chưa có ZIP, ô sẽ chỉ báo bước cần làm."),
        code('''import io, zipfile
from IPython.display import display, Image
task_name = "easy_semantic"
zip_path = exports / f"{task_name}.zip"
if zip_path.is_file():
    with zipfile.ZipFile(zip_path) as archive:
        masks = sorted(n for n in archive.namelist() if "SegmentationClass/" in n and n.endswith(".png"))
        if masks:
            print("Mask:", masks[0])
            display(Image(data=archive.read(masks[0]), width=760))
        else: print("Không có mask SegmentationClass; kiểm lại format export.")
else: print("Chưa có ZIP:", zip_path.name)
'''),
        md("## Câu hỏi tự QC\n\n1. Road và sidewalk được phân theo chức năng hay màu ảnh? 2. Có vùng nhìn thấy mà chưa gán class không? 3. Nét mảnh ở `cp3_thin` đã được xem ở mức zoom lớn chưa? Ghi lỗi và hành động sửa vào `REPORT.md`."),
    ],
    "03-qc-instance.ipynb": [
        md("# 03 · QC instance và ba checkpoint instance\n\nXuất `COCO 1.0`. Một object vật lý = một mask. Tự vẽ object Medium đầu trước gợi ý tự động và ghi quy tắc vào `REPORT.md`; gợi ý không thay quyết định của bạn. COCO `annotation_id` không phải mã object bền vững qua hai lần export."),
        code(SETUP),
        code('''instance_names = [name for name, info in tasks.items() if info["type"] == "instance"]
for name in instance_names:
    result = inspect_task(name, exports / f"{name}.zip", root)
    status = "LỖI" if result["errors"] else ("CHƯA XUẤT" if not Path(result["file"]).exists() else "OK")
    print("\\n", name, "·", status)
    print("  số annotation:", result["details"].get("annotation_count", "—"))
    print("  kiểu mask:", result["details"].get("segmentation_kinds", {}))
    for note in result["errors"]: print("  SỬA:", note)
    for note in result["warnings"]: print("  KIỂM:", note)
'''),
        md("## Đếm theo ảnh và class\n\nBảng này là số mask **bạn đã nộp**, không phải số object đúng. So lại trực quan với từng ảnh trong CVAT để tìm thiếu/thừa, gộp/tách sai, vật bị che vẫn là một object."),
        code('''task_name = "medium_instance"  # đổi thành cp1_holes, cp2_slice hoặc cp5_occlusion
result = inspect_task(task_name, exports / f"{task_name}.zip", root)
for key, count in result["details"].get("counts_by_image_class", {}).items():
    print(f"{key}: {count}")
if not result["details"].get("counts_by_image_class"): print("Chưa có object để đếm; kiểm ZIP và format.")
'''),
        md("## Ca cần phán đoán\n\n- `cp1_holes`: theo quy tắc task, kính/lỗ nằm trong mask, không tự khoét.\n- `cp2_slice`: hai xe cùng lớp sát nhau vẫn là hai instance.\n- `cp5_occlusion`: vật bị che thành hai phần nhìn thấy vẫn là một instance.\n- Nếu class sai hoặc mask ăn nền, sửa trong CVAT, Save, export lại ZIP."),
    ],
    "04-qc-panoptic.ipynb": [
        md("# 04 · QC panoptic\n\n`hard_panoptic` có hai ảnh, 12 class. Vẽ stuff (road, sky…) và từng thing (car #1, car #2…). Theo hợp đồng starter, export `COCO 1.0`; kiểm này chỉ thấy mask và class trong ZIP, **không chứng minh PQ hay mask đúng**."),
        code(SETUP),
        code('''name = "hard_panoptic"
result = inspect_task(name, exports / f"{name}.zip", root)
print("Ảnh:", result["details"].get("images", []))
print("Số mask:", result["details"].get("annotation_count", "—"))
print("Polygon/RLE:", result["details"].get("segmentation_kinds", {}))
for key, count in result["details"].get("counts_by_image_class", {}).items(): print(key, count)
for note in result["errors"]: print("SỬA:", note)
for note in result["warnings"]: print("KIỂM:", note)
'''),
        md("## Kiểm bằng mắt trong CVAT trước khi export lại\n\n1. Thing đếm được đã tách từng mask chưa? 2. Stuff có phủ phần thấy được không? 3. Có chồng lấn hoặc vùng chưa phủ ở rìa vật không? 4. Vật bị che: chỉ gán phần nhìn thấy; ghi ca mơ hồ vào report. Công cụ không tự phát hiện đầy đủ các lỗi này."),
    ],
    "05-kiem-tra-va-nop.ipynb": [
        md("# 05 · Kiểm gói nộp cuối\n\nBài nộp là **một** gói chứa `REPORT.md` và các ZIP CVAT theo tên task. Bạn có thể nộp phần hoàn thành trong 240 phút; task chưa xong cần ghi rõ trong report. Các ô dưới chỉ hỗ trợ kiểm và đóng gói, không chấm điểm."),
        code(SETUP),
        code('''from inspect_submissions import inspect_all
qc = inspect_all(exports, root)
for row in qc["tasks"]:
    status = "LỖI" if row["errors"] else ("CHƯA CÓ" if not Path(row["file"]).exists() else "OK")
    print(f"{status:7} {row['task']}")
    for error in row["errors"]: print("   !", error)
print("Lỗi hợp đồng:", qc["error_count"], "· task chưa có ZIP:", qc["missing_count"])
print("ZIP tên lạ:", qc["unknown_zips"])
'''),
        md("## Gói một file\n\nTrước tiên sao chép `reports/REPORT_TEMPLATE.md` thành `REPORT.md` ở gốc repo rồi điền thật. Chỉ chạy ô dưới khi đã có mã học viên và report. File gói cuối nằm ở gốc repo, không ở trong `submissions/`. Nếu ô báo lỗi, sửa trên CVAT và export lại."),
        code('''from package_submission import package
learner_id = ""  # điền mã học viên, ví dụ D5_012; không dùng họ tên đầy đủ
if not learner_id:
    print("Điền learner_id rồi chạy lại ô này.")
else:
    output = root / f"day5-{learner_id}.zip"
    try:
        manifest = package(exports, root / "REPORT.md", output, learner_id)
        print("Gói nộp:", output)
        print("Có:", manifest["tasks_present"])
        print("Chưa có:", manifest["tasks_missing"])
    except ValueError as exc:
        print("Chưa thể đóng gói:", exc)
'''),
        md("## Sau khi nộp\n\nGiữ bản ZIP gốc và gói đã nộp đến khi nhận phản hồi. Không chỉnh sửa export bên trong ZIP. Điểm 100 chỉ do người chấm đối chiếu reference; QC cấu trúc hoặc hai mask giống nhau không phải điểm."),
    ],
}


def main() -> None:
    outdir = ROOT / "notebooks"
    outdir.mkdir(exist_ok=True)
    for filename, cells in NOTEBOOKS.items():
        payload = {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                                                   "language_info": {"name": "python"}}, "nbformat": 4, "nbformat_minor": 5}
        (outdir / filename).write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(filename)


if __name__ == "__main__":
    main()
