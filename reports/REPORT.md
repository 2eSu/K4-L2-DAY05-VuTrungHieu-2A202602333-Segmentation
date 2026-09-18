# Báo cáo Day 5

Báo cáo ghi lại các ZIP đã chuẩn bị, quy tắc đã áp dụng và các điểm cần coach kiểm tra. Chưa tự điền điểm, PASS, top 3 hoặc bonus.

- Mã học viên theo lớp: 2A202602333
- Ngày / CVAT local: 2026-09-18 / CVAT local
- Công cụ đã dùng: Brush/Mask và Polygon; kiểm tra bằng zoom và danh sách Objects; không dùng gợi ý tự động.

Mã học viên là mã lớp cấp, không cần ghi họ tên trong bản nộp nếu kênh lớp đã nhận diện bạn. Ở dòng công cụ, giữ lại những công cụ bạn thật sự dùng; không có SAM cũng hoàn toàn bình thường.

## 1. Bài đã nộp

Các ZIP dưới đây là các file đã chuẩn bị trong workspace. Cột điểm là điểm tối đa của task, không phải điểm tự chấm.

| Task | File ZIP đúng tên | Hoàn thành mấy ảnh | Điểm tối đa (coach chấm sau) |
| --- | --- | ---: | ---: |
| easy_semantic | `easy_semantic.zip` | 3 / 3 | 20 |
| medium_instance | `medium_instance.zip` | 3 / 3 | 32 |
| hard_panoptic | `hard_panoptic.zip` | 2 / 2 | 30 |
| cp1_holes | `cp1_holes.zip` | 1 / 1 | 3 |
| cp2_slice | `cp2_slice.zip` | 1 / 1 | 3 |
| cp5_occlusion | `cp5_occlusion.zip` | 1 / 1 | 3 |
| cp3_thin | `cp3_thin.zip` | 1 / 1 | 3 |
| cp4_curb | `cp4_curb.zip` | 1 / 1 | 3 |
| cp6_coverage | `cp6_coverage.zip` | 1 / 1 | 3 |
| **Tổng tối đa** | | | **100** |

Không tự điền điểm nếu chưa có phản hồi từ người chấm. Các ZIP cần được kiểm tra trực quan trong CVAT trước khi nộp.

Không có lỗi export được xác nhận trong lần kiểm tra cấu trúc hiện tại.

## 2. Một quyết định trước khi dùng gợi ý

Object đầu tiên được tự vẽ ở `medium_instance`, trước khi xem bất kỳ đề xuất tự động nào. Quy tắc chung là vẽ phần nhìn thấy của từng vật, không đoán phần bị che.

- Ảnh, vị trí và object Medium đầu tiên tự vẽ: một `car` ở vùng nhìn thấy đầu tiên của ảnh Medium.
- Class và quy tắc tôi dùng để chọn biên: chọn `car`; mask bám phần thân xe nhìn thấy, không ăn nền và không vẽ xuyên qua xe/vật che.
- Nếu dùng gợi ý sau đó: không dùng gợi ý tự động.
- Quyết định gán nhãn: hai xe cùng class đứng sát nhau vẫn là hai mask riêng; người và phương tiện cũng là hai object riêng.

Biên mask được chọn theo phần nhìn thấy; phần bị che không được tự đoán.

## 3. Một lỗi tôi tìm thấy và sửa

Lỗi dưới đây được phát hiện khi kiểm tra export; chưa tuyên bố đã sửa trực quan trong CVAT.

- Task/ảnh/vùng: `cp1_holes`, ảnh `000000144300.jpg`, phương tiện lớn ở mép trái.
- Lỗi thuộc loại: sai lớp / biên.
- Bằng chứng tôi nhìn thấy: object có bbox rất lớn và hình dáng giống caravan/phương tiện không chắc là `car`; class list không có caravan.
- Quy tắc và hành động sửa: chỉ label vật khi nhận diện được class; không gán vật không chắc thành `car`; cần xóa hoặc vẽ lại phần đúng trong CVAT.
- Sau sửa đã Save và export lại chưa? ZIP hiện có đã được kiểm tra cấu trúc; cần xác nhận lại thao tác sửa trực quan trong CVAT trước khi nộp.

Kết quả scorer: chưa có điểm. Không tự ghi PASS, top 3 hoặc bonus; không đưa ground truth vào fork.

## 4. Ba ca chưa chắc hoặc đã cân nhắc

Các ca dưới đây là những vùng đã phải cân nhắc khi áp dụng guideline.

| Ảnh/vị trí | Hai cách hiểu có thể | Quy tắc/chứng cứ | Quyết định hoặc câu hỏi cho coach |
| --- | --- | --- | --- |
| `hard_panoptic/000000350023.jpg`, các cột đèn xa chồng lên building | Tô cột đèn vào `building` hoặc bỏ qua cột đèn | Class list không có `lamp post`; `traffic light` chỉ dành cho đèn giao thông | Tô phần building nhìn thấy, không vẽ cột đèn thành `traffic light` và không đoán phần bị che. |
| `hard_panoptic/000000460147.jpg`, truck chở nhiều car | Gộp truck và car hoặc tách từng vật | `truck` và từng `car` là các thing khác nhau; mỗi vật riêng là một instance | Tạo 1 mask `truck`, mỗi car một mask; chỉ lấy phần nhìn thấy, không vẽ xuyên qua vật che. |
| `cp4_curb`, ranh giữa road và sidewalk | Chọn theo màu hoặc theo chức năng/bó vỉa | Guideline yêu cầu xác định theo chức năng và bó vỉa, không chỉ theo màu | Chọn `sidewalk` trên phần vỉa hè/dải nâng cao và `road` trên phần xe chạy; cần coach xác nhận vùng mờ nếu ranh không rõ. |
