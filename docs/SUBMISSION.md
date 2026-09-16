# Nộp bài Day 5 — một đường dễ kiểm

Bạn làm trên CVAT local trước; notebook và lệnh dưới đây chỉ là cách tự kiểm tùy chọn. Thời gian chấm chỉ tính 240 phút trên lớp. Nếu máy không có Python, nộp trực tiếp các ZIP CVAT và `REPORT.md` theo kênh lớp thông báo; coach sẽ kiểm cấu trúc.

## 1. Xuất đúng format và đặt tên

| Task | Format trong CVAT | File sau khi đổi tên |
| --- | --- | --- |
| `easy_semantic` | Segmentation mask 1.1 | `easy_semantic.zip` |
| `medium_instance` | COCO 1.0 | `medium_instance.zip` |
| `hard_panoptic` | COCO 1.0 | `hard_panoptic.zip` |
| `cp1_holes`, `cp2_slice`, `cp5_occlusion` | COCO 1.0 | `<mã_task>.zip` |
| `cp3_thin`, `cp4_curb`, `cp6_coverage` | Segmentation mask 1.1 | `<mã_task>.zip` |

Đặt tất cả ở `submissions/` trong repo. Giữ nguyên nội dung bên trong mỗi ZIP. Nếu chưa xong trạm nào, không tạo ZIP rỗng; ghi rõ vào report.

## 2. Điền một report

Sao chép `reports/REPORT_TEMPLATE.md` thành `REPORT.md` ở gốc repo và điền mã học viên, task hoàn thành, một quyết định tự vẽ trước gợi ý, một lỗi đã sửa và ba ca cân nhắc. Không tự điền điểm. Nếu export thất bại, ghi tên task, trạng thái đã Save trên CVAT và báo coach.

## 3. Tự kiểm tùy chọn

Từ thư mục gốc repo, chạy:

```bash
python3 scripts/inspect_submissions.py --dir submissions
```

`OK` chỉ có nghĩa ZIP đọc được và khớp hợp đồng ảnh/class/mask. `THIẾU` nghĩa chưa có ZIP; đó không phải lỗi kỹ thuật. `LỖI` cần sửa trong CVAT, Save và export lại. Với COCO, dòng `annotations` là số mask đã nộp, **không phải số object đúng**. Với panoptic, phải tự xem lại phủ vùng/chồng lấn trong CVAT. Bạn cũng có thể mở năm notebook trong `notebooks/` nếu đã có Jupyter.

## 4. Đóng một gói nếu kênh nộp yêu cầu

```bash
python3 scripts/package_submission.py --learner-id D5_012
```

Lệnh tạo `day5-D5_012.zip` gồm `REPORT.md`, các export có mặt trong `exports/` và `manifest.json` có SHA-256. Gói vẫn cho phép task chưa kịp, nhưng report phải giải thích. Không nộp cả thư mục repo, ảnh gốc, file reference hay file tạm notebook.

Nếu kênh nhận nhiều file, có thể nộp `REPORT.md` cùng từng ZIP đúng tên mà không chạy lệnh. Nếu kênh nhận một file nhưng bạn không có Python, nén thủ công `REPORT.md` và các ZIP export thành một ZIP, đặt tên `day5-<mã_học_viên>.zip`; không cần tự tạo checksum. Coach chấm cùng một rubric 100 điểm, không ưu tiên cách đóng gói bằng code.
