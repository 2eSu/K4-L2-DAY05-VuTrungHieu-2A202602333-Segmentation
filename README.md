# Day 5 — Segmentation Data Lab

**Dành cho học viên · 240 phút trên lớp · tối đa 100 điểm.** Đây là một repo cho cả ngày, không có bài bắt buộc về nhà. Bài giữ nguyên cấu trúc, ảnh, lớp và trọng số của [starter Day 5](https://github.com/VinUni-AI20k/Day5-Segmentation-Data-Student) tại commit `3bff13d`: Easy semantic → Medium instance → Hard panoptic → sáu checkpoint. Hướng dẫn và đường nộp được làm rõ để học viên mới cũng có thể tự làm trên CVAT local.

**Bắt đầu tại [lab-guide.html](lab-guide.html)** để xem từng bước kèm ảnh chụp CVAT local. Nếu xem trên GitHub không mở được HTML tương tác, tải repo và mở file đó trong Chrome/Edge. Bản văn bản gọn ở [GUIDE.md](GUIDE.md); tên lớp chính xác nằm trong `classes.json` của từng task.

| Phần | Ảnh | Điểm tối đa | Export CVAT |
| --- | ---: | ---: | --- |
| `easy_semantic` | 3 | 20 | Segmentation mask 1.1 |
| `medium_instance` | 3 | 32 | COCO 1.0 |
| `hard_panoptic` | 2 | 30 | COCO 1.0 |
| `cp1_holes` … `cp6_coverage` | 1 mỗi trạm | 6 × 3 = 18 | Theo loại task trong `data/manifest.json` |
| **Tổng** | | **100** | |

## Bài nộp duy nhất

Nộp theo kênh lớp thông báo: các ZIP export CVAT đã làm, đặt đúng tên task (ví dụ `easy_semantic.zip`, `cp2_slice.zip`), và một [REPORT.md](reports/REPORT_TEMPLATE.md) đã điền. Không sửa file bên trong ZIP, không nộp ảnh đáp án, và không cần tự chạy mã chấm. Nếu không kịp task nào, ghi rõ task đó trong report; không làm tiếp ở nhà để cộng điểm.

Ground truth **không có trong repo học viên**. Người chấm giữ reference và trả điểm/phản hồi sau khi nhận bài; file `data/manifest.json` là danh sách task, không phải đáp án. Một kết quả giống bản máy hoặc bạn khác chỉ đo sự tương đồng, chưa chứng minh đúng. Cờ bất thường hay điểm rất cao cũng không tự kết luận gian lận.

## Nếu công cụ AI không có

SAM không phải điều kiện để làm lab. Dùng Brush hoặc Polygon; nếu CVAT local hiện Intelligent Scissors thì có thể thử. Khi có gợi ý tự động, bạn vẫn quyết định class, kiểm số object và sửa biên. Ở Medium, tự vẽ **một object đầu tiên** và ghi một quy tắc trước khi xem gợi ý. Xem [CVAT_SETUP.md](CVAT_SETUP.md) khi gặp lỗi công cụ.

Ai hoàn thành sớm có thể phân tích một ca mơ hồ, tìm nguyên nhân mask sai và đề xuất cách sửa. Đây là chiều sâu của cùng bài, **không có điểm cộng hay đường chấm riêng**.

