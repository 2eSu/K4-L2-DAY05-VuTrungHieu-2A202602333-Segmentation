# Báo cáo Day 5

Báo cáo ghi lại các ZIP đã chuẩn bị, quy tắc đã áp dụng và các điểm cần coach kiểm tra. Chưa tự điền điểm, PASS, top 3 hoặc bonus.

- Mã học viên theo lớp: 2A202602333
- Ngày / CVAT local: 2026-09-18 / CVAT local
- Công cụ đã dùng: Brush/Mask và Polygon; kiểm tra bằng zoom và danh sách Objects; không dùng gợi ý tự động.

Mã học viên là mã lớp cấp; không cần ghi họ tên trong report nếu kênh VLearn đã nhận diện bạn. Chỉ ghi công cụ thật sự đã dùng; không có SAM vẫn làm bài bình thường.

## 1. Bài đã nộp

Ghi tên ZIP đúng như file trong `submissions/` và số ảnh đã vẽ, Save. Chưa làm hoặc export lỗi thì ghi `chưa có`, không tạo ZIP rỗng. Cột điểm là điểm tối đa của task, **không phải điểm tự chấm**.

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

Nếu export lỗi, ghi task, dữ liệu đã Save đến đâu và lỗi đã báo coach.

## 2. Một quyết định trước khi dùng gợi ý

Object đầu tiên được tự vẽ ở `medium_instance` trước khi xem bất kỳ đề xuất tự động nào. Quy tắc chung là vẽ phần nhìn thấy của từng vật, không đoán phần bị che.

- Ảnh, vị trí và object Medium đầu tiên tự vẽ: một `car` ở vùng nhìn thấy đầu tiên của ảnh Medium.
- Class và quy tắc tôi dùng để chọn biên: chọn `car`; mask bám phần thân xe nhìn thấy, không ăn nền và không vẽ xuyên qua xe/vật che.
- Nếu dùng gợi ý sau đó: không dùng gợi ý tự động.
- Quyết định gán nhãn: hai xe cùng class đứng sát nhau vẫn là hai mask riêng; người và phương tiện cũng là hai object riêng.

## 3. Một lỗi tôi tìm thấy và sửa

Một lỗi được phát hiện khi kiểm tra export là mask `car` trong `cp1_holes` bao phủ một phương tiện lớn ở mép trái nhưng không chắc thuộc class `car`. Tôi đã ghi nhận để xóa/sửa trong CVAT thay vì ép gán class.

- Task/ảnh/vùng: `cp1_holes`, ảnh `000000144300.jpg`, phương tiện lớn ở mép trái.
- Lỗi thuộc loại: sai lớp / biên.
- Bằng chứng tôi nhìn thấy: object có bbox rất lớn và hình dáng giống caravan/phương tiện không chắc là `car`; class list không có caravan.
- Quy tắc và hành động sửa: chỉ label vật khi nhận diện được class; không gán vật không chắc thành `car`; cần xóa hoặc vẽ lại phần đúng trong CVAT.
- Sau sửa đã Save và export lại chưa? ZIP hiện có đã được kiểm tra cấu trúc; cần xác nhận lại thao tác sửa trực quan trong CVAT trước khi nộp.

Nếu bạn **đã xem Summary tự đánh giá trên GitHub Actions hoặc tự chạy script**, ghi ngắn một kết quả liên quan lỗi vừa sửa (ví dụ task, metric trước/sau nếu có): … / chưa có điểm. Scorecard ba tier tối đa **82**, không phải điểm cuối trên 100. Không tự ghi PASS/top 3/bonus; người phụ trách xác nhận theo tiêu chí lớp. Không đưa file ground truth vào fork.

## 4. Ba ca chưa chắc hoặc đã cân nhắc

Mỗi ca là một **vùng cụ thể** khiến bạn phải cân nhắc hai cách hiểu. Ghi dấu hiệu nhìn thấy hoặc quy tắc đã dùng, rồi nêu quyết định hoặc câu hỏi cho coach. Không cần ba lỗi; ca đã quyết định được cũng hợp lệ.

| Ảnh/vị trí | Hai cách hiểu có thể | Quy tắc/chứng cứ | Quyết định hoặc câu hỏi cho coach |
| --- | --- | --- | --- |
| `hard_panoptic/000000350023.jpg`, các cột đèn xa chồng lên building | Tô cột đèn vào `building` hoặc bỏ qua cột đèn | Class list chỉ có `building`, không có `lamp post`; `traffic light` chỉ dành cho đèn giao thông | Tô phần building nhìn thấy, không vẽ cột đèn thành `traffic light` và không đoán phần bị che. |
| `hard_panoptic/000000460147.jpg`, truck chở nhiều car | Gộp truck và car hoặc tách từng vật | `truck` và từng `car` là các thing khác nhau; mỗi vật riêng là một instance | Tạo 1 mask `truck`, mỗi car một mask; chỉ lấy phần nhìn thấy, không vẽ xuyên qua vật che. |
| `cp4_curb`, ranh giữa road và sidewalk | Chọn theo màu hoặc theo chức năng/bó vỉa | Guideline yêu cầu xác định theo chức năng và bó vỉa, không chỉ theo màu | Chọn `sidewalk` trên phần vỉa hè/dải nâng cao và `road` trên phần xe chạy; cần coach xác nhận vùng mờ nếu ranh không rõ. |
