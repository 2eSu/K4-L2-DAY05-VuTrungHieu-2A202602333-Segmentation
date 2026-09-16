# Notebook Day 5 — trợ lý tự kiểm, không phải bài mới

Lộ trình vẫn là 9 task của starter, 14 ảnh và 100 điểm trong 240 phút. Notebook không thêm bài, không mở đáp án, không bắt bạn viết code. Nếu mới dùng máy tính, cứ theo `lab-guide.html` và CVAT; coach có thể dùng notebook để hỗ trợ kiểm export.

| Mở khi nào | Notebook | Kết quả nhìn thấy |
| --- | --- | --- |
| Trước khi vào CVAT | `01-bat-dau-va-nhan-anh.ipynb` | Tên ảnh, class, điểm và ảnh thật của task |
| Sau Easy / semantic checkpoint | `02-qc-semantic.ipynb` | Đủ mask ảnh, labelmap và xem một PNG |
| Sau Medium / instance checkpoint | `03-qc-instance.ipynb` | Ảnh, class, số mask từng ảnh và polygon/RLE |
| Sau Hard | `04-qc-panoptic.ipynb` | Stuff/thing đã xuất và câu hỏi tự QC |
| Trước khi nộp | `05-kiem-tra-va-nop.ipynb` | Tình trạng 9 ZIP, gói nộp tùy chọn |

Mở từ gốc repo bằng JupyterLab/VS Code, hoặc từ thư mục `notebooks/`; chạy ô từ trên xuống bằng Shift+Enter. Môi trường notebook cần Python 3 và Jupyter/IPython; công cụ CLI `scripts/inspect_submissions.py` chỉ cần Python 3 chuẩn. Không cần notebook để nhận điểm. Nếu mở trong Colab, bạn phải đưa đầy đủ repo và export của **chính mình** vào cùng workspace; không upload tài liệu có thông tin cá nhân lên dịch vụ ngoài nếu quy định lớp không cho phép.

Không notebook nào tính IoU hoặc điểm khi chưa có reference. Thiếu/thừa object không thể xác định chỉ từ file của bạn: con số được in ra là **số object đã nộp**, để bạn kiểm lại bằng mắt. Nếu bạn so hai export, `annotation_id` trong COCO không phải định danh ổn định và IoU chỉ là độ giống nhau, không phải correctness.
