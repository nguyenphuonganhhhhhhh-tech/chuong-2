import streamlit as st

# Thiết lập cấu hình trang hiển thị trực quan
st.set_page_config(page_title="CHƯƠNG 2", page_icon="⏳", layout="centered")

# --- DỮ LIỆU PHẦN 1: 100 CÂU HỎI TRẮC NGHIỆM ---
quiz_data = [
    {"q": "Câu 1. Điều kiện để một phản ứng hóa học có thể tự diễn ra về mặt nhiệt động là:", "ops": ["A. ΔG > 0", "B. ΔG = 0", "C. ΔG < 0", "D. ΔH < 0 và ΔS < 0"], "ans": "C"},
    {"q": "Câu 2. Công thức tính năng lượng tự do Gibbs là:", "ops": ["A. G = H + T.S", "B. G = H − T.S", "C. G = U + T.S", "D. G = H.S − T"], "ans": "B"},
    {"q": "Câu 3. Theo Mednhicov, sự sống được định nghĩa là:", "ops": ["A. Quá trình oxy hóa liên tục các chất hữu cơ", "B. Sự duy trì và tự tái tạo một cách tích cực các cấu trúc đặc thù kèm theo tiêu tốn năng lượng", "C. Sự trao đổi chất không kèm theo năng lượng", "D. Sự cân bằng nhiệt động tuyệt đối với môi trường"], "ans": "B"},
    {"q": "Câu 4. Cơ thể sống được xem là:", "ops": ["A. Hệ nhiệt động kín, đồng thể", "B. Hệ nhiệt động mở, dị thể", "C. Hệ cô lập, đồng thể", "D. Hệ cô lập, dị thể"], "ans": "B"},
    {"q": "Câu 5. Đâu không phải là tính chất đặc trưng của sự sống được nêu trong bài?", "ops": ["A. Có cấu trúc phức tạp và tổ chức tinh vi", "B. Có sự chuyển hóa năng lượng phức tạp", "C. Thông tin của sự sống thì ổn định, chính xác và liên tục", "D. Luôn ở trạng thái cân bằng nhiệt động với môi trường"], "ans": "D"},
    {"q": "Câu 6. Cơ thể sinh vật khác với hệ mở hóa học thông thường ở điểm nào sau đây?", "ops": ["A. Cơ thể có khả năng tái tạo", "B. Cơ thể có khả năng tự phát triển", "C. Cơ thể là dạng tồn tại đặc biệt của protein và các chất tạo thành cơ thể", "D. Cả ba ý trên đều đúng"], "ans": "D"},
    {"q": "Câu 7. Nhiệt động học nghiên cứu chủ yếu về:", "ops": ["A. Cơ chế trung gian của phản ứng", "B. Trạng thái của hệ và sự bảo toàn năng lượng", "C. Tốc độ phản ứng", "D. Các yếu tố ảnh hưởng đến vận tốc phản ứng"], "ans": "B"},
    {"q": "Câu 8. Động hóa học khác với nhiệt động học ở chỗ động hóa học nghiên cứu:", "ops": ["A. Trạng thái đầu và cuối của hệ", "B. Điều kiện cân bằng của phản ứng", "C. Tốc độ và cơ chế (giai đoạn trung gian) của phản ứng", "D. Sự biến đổi công thành nhiệt"], "ans": "C"},
    {"q": "Câu 9. Động hóa học nghiên cứu điều gì là chính?", "ops": ["A. Cấu trúc phân tử của chất phản ứng", "B. Quy luật tiến triển theo thời gian và tốc độ của phản ứng hóa học", "C. Năng lượng liên kết hóa học", "D. Trạng thái cân bằng nhiệt động của hệ"], "ans": "B"},
    {"q": "Câu 10. Phản ứng hóa học được định nghĩa là:", "ops": ["A. Quá trình vật lý không làm thay đổi liên kết", "B. Quá trình chuyển đổi vật chất, các liên kết hóa học thay đổi và tạo ra chất mới", "C. Sự thay đổi trạng thái vật lý của chất", "D. Sự khuếch tán phân tử trong dung dịch"], "ans": "B"},
    {"q": "Câu 11. Tốc độ phản ứng được định nghĩa là:", "ops": ["A. Biến thiên khối lượng chất phản ứng theo thời gian", "B. Biến thiên số phân tử chất tham gia (hay tạo thành) trong một đơn vị thể tích và một đơn vị thời gian", "C. Biến thiên nhiệt độ của hệ phản ứng", "D. Biến thiên áp suất của hệ khí"], "ans": "B"},
    {"q": "Câu 12. Với phản ứng sơ cấp A → P, tốc độ phản ứng V được biểu diễn:", "ops": ["A. V = dA/dt", "B. V = -dA/dt = dP/dt", "C. V = dA/dt = dP/dt", "D. V = -dP/dt"], "ans": "B"},
    {"q": "Câu 13. Đơn vị thường dùng để biểu diễn nồng độ trong động hóa học là:", "ops": ["A. g/l", "B. mol/l", "C. mol/kg", "D. %"], "ans": "B"},
    {"q": "Câu 14. Phương pháp nào sau đây không được nêu trong bài là phương pháp nghiên cứu tốc độ phản ứng?", "ops": ["A. Stopped-flow, flash photolysis", "B. UV-Vis, IR spectrometry", "C. Đánh dấu đồng vị, đánh dấu huỳnh quang", "D. Sắc ký khí khối phổ GC-MS"], "ans": "D"},
    {"q": "Câu 15. Phương pháp Van-hoff xác định tốc độ phản ứng bằng cách:", "ops": ["A. Đo áp suất hệ phản ứng", "B. Ghi đường cong nồng độ theo thời gian và lấy tiếp tuyến tại thời điểm bất kỳ", "C. Đo pH của dung dịch", "D. Đo độ dẫn điện của dung dịch"], "ans": "B"},
    {"q": "Câu 16. Để xác định bậc phản ứng bằng thực nghiệm, người ta có thể:", "ops": ["A. Chỉ dựa vào phương trình phản ứng tổng quát", "B. Thế giá trị thực nghiệm vào các phương trình động học bậc 0,1,2,3 hoặc vẽ đồ thị C = f(t)", "C. Chỉ dựa vào số phân tử tham gia phản ứng", "D. Đo nhiệt độ phản ứng duy nhất"], "ans": "B"},
    {"q": "Câu 17. 'Phân tử số' của một phản ứng dùng để chỉ:", "ops": ["A. Số loại sản phẩm tạo thành", "B. Số phân tử tham gia vào một đơn vị cơ bản của sự chuyển hóa", "C. Bậc của phản ứng", "D. Số giai đoạn trung gian của phản ứng"], "ans": "B"},
    {"q": "Câu 18. Ba yếu tố chính ảnh hưởng đến tốc độ phản ứng được nêu trong bài là:", "ops": ["A. Nồng độ, thể tích, áp suất", "B. Nồng độ, nhiệt độ, xúc tác", "C. Nhiệt độ, áp suất, thể tích", "D. Xúc tác, khối lượng, thời gian"], "ans": "B"},
    {"q": "Câu 19. Phản ứng CH3CH2Cl → CH2=CH2 + HCl là phản ứng:", "ops": ["A. Đơn phân tử", "B. Lưỡng phân tử", "C. Tam phân tử", "D. Đa phân tử"], "ans": "A"},
    {"q": "Câu 20. Phản ứng CH3COOH + NaOH → CH3COONa + H2O thuộc loại:", "ops": ["A. Đơn phân tử", "B. Lưỡng phân tử", "C. Tam phân tử", "D. Không xác định"], "ans": "B"},
    {"q": "Câu 21. Phản ứng 2NO + O2 → 2NO2 là phản ứng:", "ops": ["A. Đơn phân tử", "B. Lưỡng phân tử", "C. Tam phân tử", "D. Tứ phân tử"], "ans": "C"},
    {"q": "Câu 22. Cách phân loại phản ứng theo 'phân tử số' dựa trên căn cứ nào?", "ops": ["A. Số lượng phân tử tham gia vào một đơn vị cơ bản của sự chuyển hóa", "B. Tổng số mũ nồng độ trong phương trình tốc độ", "C. Nhiệt độ phản ứng", "D. Bản chất xúc tác sử dụng"], "ans": "A"},
    {"q": "Câu 23. Trong sơ đồ minh họa Unimolecular – Bimolecular – Termolecular, 'Termolecular' tương ứng với:", "ops": ["A. Phản ứng đơn phân tử", "B. Phản ứng lưỡng phân tử", "C. Phản ứng tam phân tử", "D. Phản ứng không phân tử"], "ans": "C"},
    {"q": "Câu 24. Phân tử số của phản ứng luôn là:", "ops": ["A. Một số nguyên dương", "B. Có thể là số thập phân", "C. Có thể âm", "D. Luôn bằng 1"], "ans": "A"},
    {"q": "Câu 25. Nhận định nào sau đây đúng?", "ops": ["A. Phân tử số và bậc phản ứng luôn bằng nhau trong mọi trường hợp", "B. Phân tử số là khái niệm lý thuyết dựa trên cơ chế, còn bậc phản ứng là đại lượng thực nghiệm", "C. Bậc phản ứng luôn lớn hơn phân tử số", "D. Phân tử số luôn là số thập phân"], "ans": "B"},
    {"q": "Câu 26. Phản ứng tam phân tử trong thực tế thường:", "ops": ["A. Rất phổ biến vì xác suất va chạm cao", "B. Ít gặp vì xác suất ba phân tử va chạm đồng thời thấp", "C. Không tồn tại trong hóa học", "D. Chỉ xảy ra ở nhiệt độ rất thấp"], "ans": "B"},
    {"q": "Câu 27. Định luật tác dụng khối lượng (Guldberg và Waage) phát biểu tốc độ phản ứng:", "ops": ["A. V = k[A] + [B]", "B. V = k[A]^n1[B]^n2…", "C. V = k/[A][B]", "D. V = k(A+B)"], "ans": "B"},
    {"q": "Câu 28. Bậc phản ứng tổng quát n được tính bằng:", "ops": ["A. Tích các số mũ ni", "B. Tổng các số mũ ni (n = \u03a3ni)", "C. Hiệu các số mũ ni", "D. Trung bình cộng các số mũ ni"], "ans": "B"},
    {"q": "Câu 29. 'Bậc phản ứng đối với một chất cho trước' được định nghĩa là:", "ops": ["A. Số phân tử chất đó tham gia phản ứng", "B. Số mũ của nồng độ chất ấy trong phương trình động học của phản ứng", "C. Hóa trị của chất đó", "D. Khối lượng mol của chất đó"], "ans": "B"},
    {"q": "Câu 30. Hằng số k trong phương trình tốc độ phản ứng được gọi là:", "ops": ["A. Hằng số cân bằng", "B. Hằng số tốc độ phản ứng", "C. Hằng số Avogadro", "D. Hằng số khí lý tưởng"], "ans": "B"},
    {"q": "Câu 31. Bậc phản ứng có thể là:", "ops": ["A. Chỉ là số nguyên dương", "B. Số nguyên, số 0, hoặc thậm chí phân số (đối với phản ứng phức tạp)", "C. Luôn bằng phân tử số", "D. Luôn bằng 1"], "ans": "B"},
    {"q": "Câu 32. Với phản ứng aA + bB → yY + zZ ở nhiệt độ không đổi và đồng thể, đơn giản, phương trình tốc độ có dạng:", "ops": ["A. V = k[A]^a[B]^b theo đúng hệ số tỷ lượng trong mọi trường hợp", "B. V = k[A]^n1[B]^n2, trong đó n1, n2 xác định bằng thực nghiệm (không nhất thiết bằng a, b)", "C. V chỉ phụ thuộc vào nhiệt độ", "D. V không phụ thuộc nồng độ"], "ans": "B"},
    {"q": "Câu 33. Đối với phản ứng bậc 0, tốc độ phản ứng:", "ops": ["A. Tỉ lệ thuận với nồng độ chất phản ứng", "B. Không phụ thuộc vào nồng độ chất phản ứng (V = hằng số)", "C. Tỉ lệ nghịch với nồng độ chất phản ứng", "D. Tỉ lệ với bình phương nồng độ"], "ans": "B"},
    {"q": "Câu 34. Phản ứng thủy phân este RCOOR' + H2O \u2192 RCOOH + R'OH trong bài được xem là ví dụ của:", "ops": ["A. Phản ứng bậc 1", "B. Phản ứng bậc 2", "C. Phản ứng bậc 0 (do nước dư, coi nồng độ H2O không đổi)", "D. Phản ứng bậc 3"], "ans": "C"},
    {"q": "Câu 35. Trong đồ thị V theo thời gian của phản ứng bậc 0, đường biểu diễn có dạng:", "ops": ["A. Đường thẳng đi qua gốc tọa độ", "B. Đường thẳng song song với trục thời gian (hằng số)", "C. Đường cong giảm dần về 0", "D. Đường cong hàm mũ tăng"], "ans": "B"},
    {"q": "Câu 36. Vì sao nói bậc phản ứng là một đại lượng thực nghiệm chứ không phải lý thuyết thuần túy?", "ops": ["A. Vì nó luôn được suy ra trực tiếp từ phương trình hóa học cân bằng", "B. Vì nó phải xác định qua thực nghiệm đo tốc độ, có thể khác với hệ số tỷ lượng", "C. Vì nó không liên quan đến nồng độ", "D. Vì nó chỉ áp dụng cho phản ứng khí"], "ans": "B"},
    {"q": "Câu 37. Phương trình động học của phản ứng bậc 1 (A \u2192 P) là:", "ops": ["A. [A] = a \u2212 k1t", "B. [A] = a\u00b7exp(\u2212k1t)", "C. [A] = a/(1+k1t)", "D. [A] = a\u00b7k1t"], "ans": "B"},
    {"q": "Câu 38. Trong phương trình [A] = a \u2212 x của phản ứng bậc 1, 'x' đại diện cho:", "ops": ["A. Nồng độ ban đầu của A", "B. Nồng độ chất A đã phản ứng (bằng nồng độ sản phẩm tạo thành)", "C. Hằng số tốc độ", "D. Thời gian phản ứng"], "ans": "B"},
    {"q": "Câu 39. Ví dụ điển hình của phản ứng bậc 1 được nêu trong bài là:", "ops": ["A. Phản ứng ester hóa", "B. Phản ứng trung hòa acid-baz", "C. Quá trình phân rã đồng vị phóng xạ (Po \u2192 Pb + \u03b1)", "D. Phản ứng oxy hóa NO"], "ans": "C"},
    {"q": "Câu 40. Đơn vị của hằng số tốc độ k1 (phản ứng bậc 1) là:", "ops": ["A. mol/l.s", "B. s\u207b\u00b9", "C. l/mol.s", "D. l\u00b2/mol\u00b2.s"], "ans": "B"},
    {"q": "Câu 41. Đối với phản ứng bậc 2 dạng 2A \u2192 P, phương trình động học tích phân là:", "ops": ["A. k2t = 1/[A] \u2212 1/a", "B. k2t = ln(a/[A])", "C. k2t = a \u2212 [A]", "D. k2t = [A]\u00b2/a\u00b2"], "ans": "A"},
    {"q": "Câu 42. Đối với phản ứng bậc 2 dạng A + B \u2192 P (TH2, a \u2260 b), phương trình tích phân có dạng:", "ops": ["A. k2t = 1/[A] \u2212 1/a", "B. 1/(a\u2212b)\u00b7[\u2212ln(b\u2212x) + ln(a\u2212x)] = k2t + C", "C. [A] = a\u00b7exp(\u2212k2t)", "D. k2t = 1/(a\u2212b)"], "ans": "B"},
    {"q": "Câu 43. Đơn vị của hằng số tốc độ k2 (phản ứng bậc 2) là:", "ops": ["A. s\u207b\u00b9", "B. l/(mol.s)", "C. mol/(l.s)", "D. l\u00b2/mol\u00b2.s"], "ans": "B"},
    {"q": "Câu 44. Với phản ứng bậc 3 dạng 3A \u2192 P, phương trình tích phân là:", "ops": ["A. 1/[A]\u00b2 \u2212 1/a\u00b2 = 2k3t", "B. 1/[A] \u2212 1/a = k3t", "C. [A] = a\u00b7exp(\u22123k3t)", "D. ln[A] = \u2212k3t"], "ans": "A"},
    {"q": "Câu 45. Tổng quát, với phản ứng A + B + C \u2192 P (bậc 3), biểu thức tốc độ là:", "ops": ["A. V = k3", "B. V = k3[A][B][C]", "C. V = k3([A]+[B]+[C])", "D. V = k3/([A][B][C])"], "ans": "B"},
    {"q": "Câu 46. Trong bảng biến thiên của phản ứng bậc 1 (A\u2192P), khi t \u2192 \u221e thì:", "ops": ["A. [A] \u2192 a, [P] \u2192 0", "B. [A] \u2192 0, [P] \u2192 a", "C. [A] và [P] đều \u2192 a/2", "D. [A] và [P] không đổi theo thời gian"], "ans": "B"},
    {"q": "Câu 47. Thời gian bán hủy (t1/2) của phản ứng bậc 1 có đặc điểm:", "ops": ["A. Phụ thuộc vào nồng độ ban đầu a", "B. Không phụ thuộc vào nồng độ ban đầu, chỉ phụ thuộc vào k1", "C. Luôn bằng 1/k1", "D. Luôn bằng k1"], "ans": "B"},
    {"q": "Câu 48. Nếu vẽ đồ thị ln[A] theo thời gian t của một phản ứng và thu được đường thẳng, có thể kết luận:", "ops": ["A. Phản ứng có bậc 0", "B. Phản ứng có bậc 1", "C. Phản ứng có bậc 2", "D. Phản ứng có bậc 3"], "ans": "B"},
    {"q": "Câu 49. Nếu đồ thị 1/[A] theo t là đường thẳng, phản ứng đó có bậc:", "ops": ["A. 0", "B. 1", "C. 2", "D. 3"], "ans": "C"},
    {"q": "Câu 50. Nếu đồ thị 1/[A]\u00b2 theo t là đường thẳng, phản ứng có bậc:", "ops": ["A. 1", "B. 2", "C. 3", "D. 0"], "ans": "C"},
    {"q": "Câu 51. Trong phản ứng bậc 2 dạng A + B \u2192 P với a = b (nồng độ ban đầu bằng nhau), phương trình động học rút gọn tương đương với:", "ops": ["A. Dạng của phản ứng bậc 1", "B. Dạng của phản ứng 2A \u2192 P (TH1)", "C. Dạng của phản ứng bậc 3", "D. Dạng của phản ứng bậc 0"], "ans": "B"},
    {"q": "Câu 52. Một phản ứng có phương trình tốc độ V = k[A] được xác định là phản ứng:", "ops": ["A. Bậc 0", "B. Bậc 1", "C. Bậc 2", "D. Bậc 3"], "ans": "B"},
    {"q": "Câu 53. Một phản ứng có phương trình tốc độ V = k[A][B] (a \u2260 b) là phản ứng:", "ops": ["A. Bậc 0", "B. Bậc 1", "C. Bậc 2", "D. Bậc 3"], "ans": "C"},
    {"q": "Câu 54. Đặc điểm chung để phân biệt bậc phản ứng qua thực nghiệm là:", "ops": ["A. Quan sát màu sắc dung dịch", "B. Dựa vào dạng đường cong nồng độ – thời gian phù hợp với phương trình động học tương ứng", "C. Đo khối lượng riêng", "D. Đo độ nhớt dung dịch"], "ans": "B"},
    {"q": "Câu 55. Phản ứng phân rã phóng xạ Po \u2192 Pb (bền) + \u03b1 tuân theo quy luật:", "ops": ["A. Bậc 0", "B. Bậc 1 (hàm mũ giảm theo thời gian)", "C. Bậc 2", "D. Bậc 3"], "ans": "B"},
    {"q": "Câu 56. Hệ số nhiệt độ \u03b3 trong định luật Van't Hoff được định nghĩa:", "ops": ["A. \u03b3 = kt / kt+10", "B. \u03b3 = kt+10 / kt", "C. \u03b3 = kt \u00d7 kt+10", "D. \u03b3 = kt + kt+10"], "ans": "B"},
    {"q": "Câu 57. Theo Van't Hoff (1879), với phản ứng đồng thể, hệ số nhiệt độ \u03b3 thường có giá trị trong khoảng:", "ops": ["A. 0,5 – 1", "B. 1 – 2", "C. 2 – 4", "D. 5 – 10"], "ans": "C"},
    {"q": "Câu 58. Phương trình Arrhenius (1889) có dạng:", "ops": ["A. k = A + Ea/RT", "B. k = A\u00b7e^(\u2212Ea/RT)", "C. k = Ea\u00b7e^(\u2212A/RT)", "D. k = A\u00b7e^(Ea/RT)"], "ans": "B"},
    {"q": "Câu 59. Trong phương trình Arrhenius, 'A' được gọi là:", "ops": ["A. Năng lượng hoạt hóa", "B. Thừa số thực nghiệm (thừa số tần số), không phụ thuộc vào T", "C. Hằng số khí lý tưởng", "D. Hằng số cân bằng"], "ans": "B"},
    {"q": "Câu 60. 'Ea' trong phương trình Arrhenius là:", "ops": ["A. Năng lượng tự do Gibbs", "B. Năng lượng hoạt hóa thực nghiệm", "C. Nội năng của hệ", "D. Entropy hoạt hóa"], "ans": "B"},
    {"q": "Câu 61. Dạng logarit của phương trình Arrhenius là:", "ops": ["A. lnk = Ea/RT + lnA", "B. lnk = \u2212Ea/RT + lnA", "C. lnk = A/RT \u2212 Ea", "D. lnk = \u2212A/Ea + lnT"], "ans": "B"},
    {"q": "Câu 62. Khi vẽ đồ thị lnk theo 1/T, theo phương trình Arrhenius, đường biểu diễn có dạng:", "ops": ["A. Đường thẳng có độ dốc dương", "B. Đường thẳng có độ dốc âm (bằng \u2212Ea/R)", "C. Đường cong parabol", "D. Đường hyperbol"], "ans": "B"},
    {"q": "Câu 63. Sự phân bố phân tử theo năng lượng được mô tả bằng phương trình:", "ops": ["A. Phương trình Arrhenius", "B. Phương trình Maxwell–Boltzmann (NE = N\u00b7e^(\u2212E/RT))", "C. Phương trình Michaelis–Menten", "D. Phương trình Van't Hoff"], "ans": "B"},
    {"q": "Câu 64. Theo phân bố Maxwell–Boltzmann, chỉ những phân tử có năng lượng như thế nào mới có khả năng tham gia phản ứng?", "ops": ["A. E < Ea", "B. E = 0", "C. E \u2265 Ea (bằng hay lớn hơn năng lượng hoạt hóa)", "D. E bất kỳ, không cần điều kiện"], "ans": "C"},
    {"q": "Câu 65. Trên giản đồ năng lượng phản ứng (năng lượng theo diễn biến phản ứng), đỉnh cao nhất của đường cong tương ứng với:", "ops": ["A. Trạng thái sản phẩm bền", "B. Trạng thái chất đầu", "C. Trạng thái chuyển tiếp (phức hoạt hóa, năng lượng cực đại E*)", "D. Điểm cân bằng của phản ứng"], "ans": "C"},
    {"q": "Câu 66. Khi nhiệt độ tăng, theo Arrhenius, hằng số tốc độ k thường:", "ops": ["A. Giảm", "B. Tăng", "C. Không đổi", "D. Có thể tăng hoặc giảm ngẫu nhiên"], "ans": "B"},
    {"q": "Câu 67. Một trong ba dạng đồ thị v theo T (I, II, III) trong bài minh họa cho:", "ops": ["A. Phản ứng luôn tăng tốc độ đều đặn theo T ở mọi trường hợp mà không có ngoại lệ", "B. Các kiểu ảnh hưởng khác nhau của nhiệt độ đến tốc độ phản ứng (kể cả trường hợp v tăng rồi giảm - dạng III, thường gặp ở enzym)", "C. Sự phụ thuộc của áp suất vào nhiệt độ", "D. Sự phụ thuộc của bậc phản ứng vào nhiệt độ"], "ans": "B"},
    {"q": "Câu 68. Năng lượng hoạt hóa Ea càng lớn thì:", "ops": ["A. Phản ứng xảy ra càng nhanh ở cùng nhiệt độ", "B. Phản ứng càng nhạy với sự thay đổi nhiệt độ (k thay đổi mạnh khi T thay đổi)", "C. Phản ứng không phụ thuộc nhiệt độ", "D. Hằng số cân bằng luôn bằng 1"], "ans": "B"},
    {"q": "Câu 69. Phản ứng thuận nghịch là phản ứng:", "ops": ["A. Chỉ diễn ra theo một chiều duy nhất", "B. Diễn ra theo hai chiều ngược nhau (thuận và nghịch) đồng thời", "C. Không có sản phẩm tạo thành", "D. Chỉ xảy ra trong pha khí"], "ans": "B"},
    {"q": "Câu 70. Với phản ứng thuận nghịch aA + bB \u21cc xX + yY (k1; k2), hằng số cân bằng K được tính:", "ops": ["A. K = k1 + k2", "B. K = k1/k2", "C. K = k1 \u00d7 k2", "D. K = k2/k1"], "ans": "B"},
    {"q": "Câu 71. Tại trạng thái cân bằng của phản ứng thuận nghịch:", "ops": ["A. Vt > Vn", "B. Vt < Vn", "C. Vt = Vn", "D. Vt = 0 và Vn = 0"], "ans": "C"},
    {"q": "Câu 72. Tốc độ thực (Vtp) của phản ứng thuận nghịch được tính bằng:", "ops": ["A. Vtp = Vt + Vn", "B. Vtp = Vt \u2212 Vn", "C. Vtp = Vt \u00d7 Vn", "D. Vtp = Vt/Vn"], "ans": "B"},
    {"q": "Câu 73. Phản ứng nối tiếp là phản ứng trong đó:", "ops": ["A. Các chất phản ứng tương tác đồng thời độc lập với nhau", "B. Chất phản ứng biến hóa thành sản phẩm qua nhiều giai đoạn nối tiếp nhau", "C. Sản phẩm quay lại tạo thành chất đầu", "D. Chỉ có một giai đoạn duy nhất"], "ans": "B"},
    {"q": "Câu 74. Với phản ứng nối tiếp bậc 1: A \u2192 B \u2192 C (k1; k2), tại t=0 có [A]=a, [B]=[C]=0. Biểu thức [A] theo thời gian là:", "ops": ["A. [A] = a \u2212 k1t", "B. [A] = a\u00b7e^(\u2212k1t)", "C. [A] = a/(1+k1t)", "D. [A] = a\u00b7e^(k1t)"], "ans": "B"},
    {"q": "Câu 75. Trong phản ứng nối tiếp A\u2192B\u2192C, thời điểm nồng độ B đạt cực đại (tmax) được tính bằng:", "ops": ["A. tmax = 1/(k2\u2212k1)\u00b7ln(k2/k1)", "B. tmax = (k2\u2212k1)\u00b7ln(k1/k2)", "C. tmax = k1\u00d7k2", "D. tmax = 1/(k1+k2)"], "ans": "A"},
    {"q": "Câu 76. Trong đồ thị phản ứng nối tiếp A\u2192B\u2192C theo thời gian, đường biểu diễn của B thường có dạng:", "ops": ["A. Giảm liên tục về 0", "B. Tăng liên tục đến giá trị a", "C. Tăng đến cực đại rồi giảm dần", "D. Không đổi theo thời gian"], "ans": "C"},
    {"q": "Câu 77. Phản ứng song song là các phản ứng:", "ops": ["A. Phụ thuộc lẫn nhau và diễn ra tuần tự", "B. Độc lập, đồng thời, xuất phát từ cùng một (hay nhiều) chất đầu, tốc độ khác nhau", "C. Chỉ có một sản phẩm duy nhất", "D. Luôn có cùng hằng số tốc độ"], "ans": "B"},
    {"q": "Câu 78. Với phản ứng song song A \u2192 B (k1) và A \u2192 C (k2), tỉ lệ sản phẩm b/c bằng:", "ops": ["A. k1 + k2", "B. k1/k2", "C. k1 \u00d7 k2", "D. k2 \u2212 k1"], "ans": "B"},
    {"q": "Câu 79. Khi các phản ứng song song có tốc độ khác nhau rất nhiều, phản ứng chính được xem là:", "ops": ["A. Phản ứng có tốc độ nhỏ nhất", "B. Phản ứng có tốc độ lớn nhất", "C. Cả hai phản ứng đều là phản ứng chính", "D. Không xác định được phản ứng chính"], "ans": "B"},
    {"q": "Câu 80. Phản ứng vòng là phản ứng mà tốc độ chu trình phụ thuộc vào:", "ops": ["A. Nồng độ tuyệt đối của chất ban đầu duy nhất", "B. Nồng độ tương đối của các chất tham gia vào từng giai đoạn trong chu trình", "C. Chỉ phụ thuộc vào nhiệt độ", "D. Không phụ thuộc vào bất kỳ yếu tố nào"], "ans": "B"},
    {"q": "Câu 81. Dạng đơn giản nhất của phản ứng vòng được nêu trong bài là:", "ops": ["A. Phản ứng thuận nghịch", "B. Phản ứng dây chuyền", "C. Phản ứng men (enzym xúc tác)", "D. Phản ứng tự xúc tác"], "ans": "C"},
    {"q": "Câu 82. Trong sơ đồ phản ứng men E + S \u21cc ES \u2192 E + P, các ký hiệu lần lượt là:", "ops": ["A. E: sản phẩm, S: enzym, P: cơ chất", "B. E: enzym, S: cơ chất (Substrate), P: sản phẩm (Product)", "C. E: phức chất, S: enzym, P: cơ chất", "D. E: cơ chất, S: sản phẩm, P: enzym"], "ans": "B"},
    {"q": "Câu 83. Chu trình acid citric (Citric acid cycle) được nêu trong bài như một ví dụ minh họa cho:", "ops": ["A. Phản ứng thuận nghịch đơn giản", "B. Phản ứng vòng (chu trình sinh học nhiều giai đoạn nối tiếp khép kín)", "C. Phản ứng bậc 0", "D. Phản ứng dây chuyền phân nhánh"], "ans": "B"},
    {"q": "Câu 84. Trong 4 loại phản ứng phức tạp (thuận nghịch, nối tiếp, song song, vòng), phản ứng nào có đặc điểm sản phẩm cuối có thể quay lại tương tác tạo chất đầu?", "ops": ["A. Phản ứng nối tiếp", "B. Phản ứng thuận nghịch", "C. Phản ứng song song", "D. Phản ứng vòng"], "ans": "D"},
    {"q": "Câu 85. Nếu k2 \u226b k1 trong phản ứng nối tiếp A\u2192B\u2192C, thì:", "ops": ["A. Giai đoạn quyết định tốc độ chung là giai đoạn A\u2192B (chậm nhất)", "B. Giai đoạn quyết định tốc độ chung là giai đoạn B\u2192C", "C. Cả hai giai đoạn đều quyết định tốc độ như nhau", "D. Không thể xác định giai đoạn quyết định tốc độ"], "ans": "A"},
    {"q": "Câu 86. Câu nào sau đây đúng khi so sánh phản ứng nối tiếp và phản ứng song song?", "ops": ["A. Nối tiếp: sản phẩm hình thành qua các giai đoạn kế tiếp; Song song: nhiều phản ứng độc lập xảy ra đồng thời từ cùng chất đầu", "B. Nối tiếp và song song là một, không có gì khác biệt", "C. Song song luôn nhanh hơn nối tiếp", "D. Nối tiếp luôn không có chất trung gian"], "ans": "A"},
    {"q": "Câu 87. Trong phản ứng thuận nghịch, nếu k1 \u226b k2 (k1: chiều thuận, k2: chiều nghịch), điều đó cho thấy:", "ops": ["A. Cân bằng nghiêng mạnh về phía sản phẩm (chiều thuận chiếm ưu thế)", "B. Cân bằng nghiêng mạnh về phía chất đầu", "C. Phản ứng không đạt cân bằng", "D. K = 0"], "ans": "A"},
    {"q": "Câu 88. Trong chu trình acid citric, chất nào đóng vai trò 'tái sinh' để khép kín vòng phản ứng?", "ops": ["A. Citrate", "B. Oxaloacetate", "C. Pyruvate", "D. Acetyl-CoA"], "ans": "B"},
    {"q": "Câu 89. Phản ứng dây chuyền được xem là:", "ops": ["A. Phản ứng đơn giản một giai đoạn", "B. Phản ứng nối tiếp đặc biệt với hợp chất trung gian là các tiểu phân hoạt hóa cao (nguyên tử, gốc tự do)", "C. Phản ứng chỉ xảy ra ở pha rắn", "D. Phản ứng không có giai đoạn trung gian"], "ans": "B"},
    {"q": "Câu 90. Ba giai đoạn cơ bản trong cơ chế phản ứng dây chuyền là:", "ops": ["A. Sinh mạch, phát triển mạch, cắt mạch (đứt mạch)", "B. Khởi đầu, cân bằng, kết thúc", "C. Tạo phức, phân ly, tái hợp", "D. Hấp phụ, phản ứng bề mặt, giải hấp"], "ans": "A"},
    {"q": "Câu 91. Đặc điểm nhạy cảm với chất lạ của phản ứng dây chuyền thể hiện qua ví dụ nào?", "ops": ["A. Phản ứng ester hóa không đổi khi thêm chất xúc tác", "B. Hỗn hợp khí Cl2 và H2 trong bóng tối không phản ứng, nhưng phản ứng mãnh liệt khi có một lượng nhỏ Natri", "C. Phản ứng trung hòa acid-baz không đổi khi có mặt muối", "D. Phản ứng phân rã phóng xạ không đổi theo chất xúc tác"], "ans": "B"},
    {"q": "Câu 92. Phản ứng dây chuyền không phân nhánh có đặc điểm:", "ops": ["A. Một tiểu phân hoạt động mất đi sinh ra hai tiểu phân hoạt động mới", "B. Một tiểu phân hoạt động mất đi chỉ sinh ra một tiểu phân hoạt động mới", "C. Số tiểu phân hoạt động luôn giảm về 0 ngay lập tức", "D. Không có tiểu phân hoạt động nào được sinh ra"], "ans": "B"},
    {"q": "Câu 93. Phản ứng dây chuyền phân nhánh (ví dụ: phản ứng cháy H2 với O2) có đặc điểm:", "ops": ["A. Số tiểu phân hoạt động tăng theo hàm số mũ do một tiểu phân sinh ra hai (hoặc nhiều) tiểu phân mới", "B. Số tiểu phân hoạt động luôn không đổi", "C. Không có hiện tượng nổ xảy ra", "D. Bậc phản ứng luôn là số nguyên xác định"], "ans": "A"},
    {"q": "Câu 94. Đặc điểm nào sau đây không đúng với phản ứng dây chuyền?", "ops": ["A. Tốc độ phụ thuộc vào hình dạng, kích thước, vật liệu bình phản ứng", "B. Bậc phản ứng có thể là phân số", "C. Thường kèm theo hiện tượng nổ", "D. Hoàn toàn không nhạy cảm với tạp chất"], "ans": "D"},
    {"q": "Câu 95. Trong ví dụ H2 + O2 \u2192 2OH (giai đoạn sinh mạch), các phản ứng OH + H2 \u2192 H2O + H, H + O2 \u2192 OH + O, O + H2 \u2192 OH + H thuộc giai đoạn nào?", "ops": ["A. Giai đoạn sinh mạch", "B. Giai đoạn phát triển mạch (mắt xích)", "C. Giai đoạn cắt mạch", "D. Giai đoạn cân bằng"], "ans": "B"},
    {"q": "Câu 96. Chất xúc tác được định nghĩa là chất:", "ops": ["A. Làm thay đổi tốc độ phản ứng, sau phản ứng bản chất hóa học và lượng của nó không đổi", "B. Bị tiêu hao hoàn toàn sau phản ứng", "C. Chỉ làm tăng tốc độ phản ứng thuận mà không ảnh hưởng phản ứng nghịch", "D. Làm thay đổi giới hạn (hằng số cân bằng) của phản ứng"], "ans": "A"},
    {"q": "Câu 97. Đối với phản ứng thuận nghịch, chất xúc tác:", "ops": ["A. Chỉ làm tăng tốc độ phản ứng thuận", "B. Làm tăng tốc độ cả phản ứng thuận và nghịch, giúp nhanh đạt cân bằng, không đổi hằng số cân bằng", "C. Làm thay đổi hằng số cân bằng K", "D. Không có tác dụng gì với phản ứng thuận nghịch"], "ans": "B"},
    {"q": "Câu 98. Cơ chế xúc tác đồng thể hoạt động bằng cách:", "ops": ["A. Không tham gia vào phản ứng, chỉ hấp phụ bề mặt", "B. Tham gia vào phản ứng, tạo sản phẩm trung gian, hướng phản ứng theo con đường có năng lượng hoạt hóa thấp hơn", "C. Làm tăng năng lượng hoạt hóa của phản ứng", "D. Chỉ có tác dụng vật lý, không có ý nghĩa hóa học"], "ans": "B"},
    {"q": "Câu 99. Theo phương trình Michaelis–Menten, tốc độ phản ứng enzym V được biểu diễn:", "ops": ["A. V = Vmax\u00b7[S]/(Km + [S])", "B. V = Vmax\u00b7Km/[S]", "C. V = Vmax + Km\u00b7[S]", "D. V = Vmax \u2212 Km/[S]"], "ans": "A"},
    {"q": "Câu 100. Hằng số Michaelis–Menten Km được định nghĩa (theo cơ chế E+S\u21ccES\u2192E+P với k1, k2, k3) là:", "ops": ["A. Km = k1 + k2 + k3", "B. Km = (k2 + k3)/k1", "C. Km = k1/(k2+k3)", "D. Km = k1\u00b7k2\u00b7k3"], "ans": "B"}
]

# --- DỮ LIỆU PHẦN 2: 30 CÂU HỎI ĐIỀN TỪ ---
fill_data = [
    {"q": "1. Điều kiện để phản ứng diễn ra tự nhiên về mặt nhiệt động là G = H \u2212 T.S __________ 0.", "ans": "<"},
    {"q": "2. Theo Mednhicov, sự sống là 'sự duy trì và __________ một cách tích cực các cấu trúc đặc thù kèm theo tiêu tốn năng lượng'.", "ans": "tự tái tạo"},
    {"q": "3. Cơ thể sống là hệ nhiệt động __________, dị thể.", "ans": "mở"},
    {"q": "4. Động hóa học nghiên cứu những cơ chế và quy luật __________ theo thời gian của các quá trình hóa học.", "ans": "tiến triển"},
    {"q": "5. Tốc độ phản ứng là biến thiên của số phân tử chất tham gia (hay tạo thành) trong một đơn vị __________ và trong một đơn vị __________.", "ans": "thể tích / thời gian", "alt": ["thể tích, thời gian", "thể tích và thời gian"]},
    {"q": "6. With phản ứng A \u2192 P, biểu thức tốc độ được viết: V = __________ = dP/dt.", "ans": "\u2212dA/dt"},
    {"q": "7. Phản ứng đơn phân tử, lưỡng phân tử, tam phân tử được phân loại dựa trên căn cứ __________ tham gia vào một đơn vị cơ bản của chuyển hóa.", "ans": "số lượng phân tử", "alt": ["phân tử số"]},
    {"q": "8. Theo định luật tác dụng khối lượng của Guldberg và Waage: V = k[A]^n1[B]^n2…, trong đó bậc phản ứng n = __________.", "ans": "\u03a3ni", "alt": ["tổng các số mũ"]},
    {"q": "9. 'Bậc phản ứng đối với một chất cho trước là số __________ của nồng độ chất ấy trong phương trình động học của phản ứng'.", "ans": "mũ"},
    {"q": "10. Với phản ứng bậc 1: A \u2192 P, ta có [A] = a.exp(__________).", "ans": "\u2212k1t"},
    {"q": "11. Với phản ứng bậc 0, tốc độ V = d[este]/dt = k[este][H2O] = __________.", "ans": "hằng số", "alt": ["const"]},
    {"q": "12. Hệ số nhiệt độ Van't Hoff được ký hiệu \u03b3 = k(t+10)/kt, với phản ứng đồng thể \u03b3 thường trong khoảng __________.", "ans": "2\u20134", "alt": ["2-4"]},
    {"q": "13. Phương trình Arrhenius có dạng: k = A.e^(__________).", "ans": "\u2212Ea/RT"},
    {"q": "14. Trong phương trình Arrhenius, Ea được gọi là năng lượng __________.", "ans": "hoạt hóa"},
    {"q": "15. Sự phân bố phân tử theo năng lượng được mô tả bằng phương trình __________.", "ans": "Maxwell\u2013Boltzmann", "alt": ["Maxwell Boltzmann"]},
    {"q": "16. Chỉ có phân tử có năng lượng bằng hay lớn hơn năng lượng hoạt hóa Ea mới có khả năng __________ phản ứng.", "ans": "tham gia"},
    {"q": "17. Phản ứng __________ là phản ứng diễn ra theo hai chiều ngược nhau đồng thời.", "ans": "thuận nghịch"},
    {"q": "18. Tại trạng thái cân bằng của phản ứng thuận nghịch, Vt __________ Vn.", "ans": "=", "alt": ["bằng"]},
    {"q": "19. Phản ứng __________ là phản ứng trong đó chất phản ứng biến hóa thành sản phẩm qua nhiều giai đoạn kế tiếp nhau.", "ans": "nối tiếp"},
    {"q": "20. Phản ứng __________ là những phản ứng độc lập, đồng thời, xuất phát từ cùng một hay nhiều chất đầu, diễn ra với tốc độ khác nhau.", "ans": "song song"},
    {"q": "21. Tốc độ chu trình của phản ứng vòng phụ thuộc vào nồng độ __________ của các chất tham gia vào từng giai đoạn trong chu trình.", "ans": "tương đối"},
    {"q": "22. Trong sơ đồ phản ứng men, E là __________, S là cơ chất, P là __________.", "ans": "enzym / sản phẩm", "alt": ["enzym, sản phẩm"]},
    {"q": "23. Phản ứng dây chuyền được coi là phản ứng nối tiếp đặc biệt, trong đó hợp chất trung gian là những __________ hoạt hóa cao.", "ans": "tiểu phân"},
    {"q": "24. Ba giai đoạn cơ bản của phản ứng dây chuyền gồm: sinh mạch, __________, và cắt mạch.", "ans": "phát triển mạch"},
    {"q": "25. Phản ứng dây chuyền __________ là phản ứng trong đó một tiểu phân hoạt động mất đi tạo ra hai (hoặc nhiều) tiểu phân hoạt động mới.", "ans": "phân nhánh"},
    {"q": "26. Chất __________ là chất làm thay đổi tốc độ phản ứng nhưng sau phản ứng bản chất hóa học và lượng của nó không đổi.", "ans": "xúc tác"},
    {"q": "27. Xúc tác đồng thể tăng tốc độ phản ứng bằng cách tạo sản phẩm trung gian, hướng phản ứng đi theo con đường có năng lượng hoạt hóa __________ hơn.", "ans": "thấp"},
    {"q": "28. Enzym có bản chất là __________.", "ans": "protein"},
    {"q": "29. Hằng số Michaelis-Menten được ký hiệu là __________, bằng (k2+k3)/k1.", "ans": "Km"},
    {"q": "30. Phản ứng __________ là phản ứng mà sản phẩm của phản ứng giữ vai trò chất xúc tác cho chính phản ứng đó (ví dụ: Pepxinogen \u2192 Pepxin).", "ans": "tự xúc tác", "alt": ["autocatalysis"]}
]

# --- QUẢN LÝ TRẠNG THÁI (SESSION STATE) ---
if 'answers_a' not in st.session_state:
    st.session_state.answers_a = [None] * len(quiz_data)
if 'answers_b' not in st.session_state:
    st.session_state.answers_b = [""] * len(fill_data)

# --- THIẾT KẾ SIDEBAR MENU ---
st.sidebar.title("🧭 Chọn phần ôn tập")
menu = st.sidebar.radio("Chuyển nhanh tới mục:", ["Phần 1: Trắc nghiệm (100 câu)", "Phần 2: Điền từ (30 câu)"])

# --- GIAO DIỆN CHÍNH ---
st.title("⏳ ĐỘNG HÓA HỌC CÁC QUÁ TRÌNH SINH HỌC")
st.caption("Dữ liệu đồng bộ tự động, chấm điểm thực thời bám sát cấu trúc của tệp 'Câu hỏi chương 2_2.docx'[cite: 7]")
st.markdown("---")

# 1. LOGIC XỬ LÝ PHẦN 1: TRẮC NGHIỆM CHẤM ĐIỂM NGAY TẠI CHỖ
if menu == "Phần 1: Trắc nghiệm (100 câu)":
    st.header("📝 PHẦN 1: CÂU HỎI TRẮC NGHIỆM TỰ ĐỘNG CHẤM")
    st.info("Hệ thống hiển thị kết quả đúng/sai ngay sau khi bạn tích chọn câu trả lời.")

    def render_quiz_block(start, end, section_title):
        st.subheader(section_title)
        for i in range(start, end):
            item = quiz_data[i]
            saved_idx = st.session_state.answers_a[i]
            
            user_choice = st.radio(
                item["q"], 
                item["ops"], 
                index=saved_idx, 
                key=f"mcq_{i}", 
                horizontal=True
            )
            
            if user_choice is not None:
                st.session_state.answers_a[i] = item["ops"].index(user_choice)
                
                # Trích xuất ký tự đầu tiên (A, B, C, D) để kiểm tra tính chính xác[cite: 7]
                if user_choice[0] == item["ans"]:
                    st.success(f"✅ Đúng! Đáp án chính xác: **{item['ans']}**")
                else:
                    st.error(f"❌ Chưa chính xác. Đáp án đúng: **{item['ans']}**")
            st.markdown("<hr style='margin: 10px 0px; border-top: 1px dashed #bbb;'>", unsafe_allow_html=True)

    render_quiz_block(0, 8, "A. Nhiệt động học & Cơ thể sống (Câu 1–8)[cite: 7]")
    render_quiz_block(8, 18, "B. Khái niệm cơ bản của động hóa học (Câu 9–18)[cite: 7]")
    render_quiz_block(18, 26, "C. Phân loại phản ứng theo phân tử số (Câu 19–26)[cite: 7]")
    render_quiz_block(26, 36, "D. Bậc phản ứng và định luật tác dụng khối lượng (Câu 27–36)[cite: 7]")
    render_quiz_block(36, 55, "E. Phản ứng bậc 1, bậc 2, bậc 3 (Câu 37–55)[cite: 7]")
    render_quiz_block(55, 68, "F. Ảnh hưởng của nhiệt độ đến tốc độ phản ứng (Câu 56–68)[cite: 7]")
    render_quiz_block(68, 88, "G. Phản ứng phức tạp: thuận nghịch, nối tiếp, song song, vòng (Câu 69–88)[cite: 7]")
    render_quiz_block(88, 95, "H. Phản ứng dây chuyền (Câu 89–95)[cite: 7]")
    render_quiz_block(95, 100, "I. Xúc tác và Enzym (Câu 96–100)[cite: 7]")

# 2. LOGIC XỬ LÝ PHẦN 2: ĐIỀN TỪ CHẤM ĐIỂM KHI ẤN ENTER
elif menu == "Phần 2: Điền từ (30 câu)":
    st.header("✏️ PHẦN 2: CÂU HỎI ĐIỀN TỪ / CỤM TỪ TỰ ĐỘNG CHẤM[cite: 7]")
    st.info("Nhập từ hoặc cụm từ thích hợp vào ô trống rồi nhấn phím **Enter** trên bàn phím để đối chiếu đáp án.")
    
    for i, item in enumerate(fill_data):
        input_val = st.text_input(item["q"], value=st.session_state.answers_b[i], key=f"fld_{i}").strip()
        st.session_state.answers_b[i] = input_val
        
        if input_val != "":
            student_text = input_val.lower()
            correct_text = item["ans"].lower()
            
            # Kiểm tra so khớp đáp án chính xác hoặc các phương án phụ đồng nghĩa đã được khai báo[cite: 7]
            match = (student_text == correct_text)
            if "alt" in item:
                for alternative in item["alt"]:
                    if student_text == alternative.lower():
                        match = True
                        
            if match:
                st.success(f"✅ Chính xác! Đáp án đúng: **{item['ans']}**")
            else:
                st.error(f"❌ Chưa chính xác. Đáp án đúng là: **{item['ans']}**")
        st.write("")
