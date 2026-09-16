# Rubric Day 5 — tối đa 100 điểm trong lớp

Trọng số giữ từ [starter Day 5](https://github.com/VinUni-AI20k/Day5-Segmentation-Data-Student) commit `3bff13d`; không có bài về nhà hoặc điểm cộng. Task chưa nộp được ghi là chưa có bằng chứng, không tự điền điểm giả. Bản nộp được xem cùng ảnh, class và quy tắc của task; reference để chấm do người phụ trách giữ riêng.

| Task | Loại | Điểm tối đa | Điều cần chứng minh |
| --- | --- | ---: | --- |
| `easy_semantic` | Semantic | 20 | Phủ đúng vùng và lớp, nhất là road/sidewalk |
| `medium_instance` | Instance | 32 | Đủ vật, đúng class, từng vật một mask, biên theo phần nhìn thấy |
| `hard_panoptic` | Panoptic | 30 | Stuff và things cùng đúng; things tách instance, ít vùng bỏ trống/chồng lấn |
| Sáu checkpoint | Theo từng trạm | 6 × 3 = 18 | Xử lý lỗ, tách, nét mảnh, bó vỉa, che khuất, phủ vùng |
| **Tổng** | | **100** | |

Metric của starter gồm mIoU/coverage cho semantic, matched IoU và recall cho instance, PQ cho panoptic. **Chỉ có thể tính điểm so reference khi người chấm có ground truth phù hợp.** IoU giữa hai bản nhãn hoặc với gợi ý máy chỉ là độ giống nhau, không phải correctness. Điểm, cờ bất thường hoặc tốc độ không tự chứng minh người học gian lận; khi cần coach xem lại cách áp dụng quy tắc và bằng chứng trước/sau sửa.

Mọi học viên có cùng bài, lớp và chuẩn bằng chứng. Hướng dẫn trực quan giúp người mới thao tác; người xong sớm phân tích lỗi khó hơn nhưng không nhận thêm điểm. Dùng công cụ hỗ trợ không thay thế việc tự kiểm và giải thích một quyết định gán nhãn.

