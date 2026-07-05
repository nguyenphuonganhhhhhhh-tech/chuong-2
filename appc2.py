import streamlit as st

# Thiết lập cấu hình trang
st.set_page_config(page_title="Ôn tập Nhiệt động học", page_icon="🌡️", layout="centered")

# --- DỮ LIỆU PHẦN A: 100 CÂU HỎI TRẮC NGHIỆM ---
quiz_data = [
    {"q": "Câu 1. Nhiệt động học là môn khoa học nghiên cứu về?", "ops": ["A. Sự biến đổi năng lượng", "B. Cấu trúc tế bào", "C. Di truyền học", "D. Quang hợp"], "ans": "A"},
    {"q": "Câu 2. Hệ không trao đổi vật chất và năng lượng với môi trường được gọi là?", "ops": ["A. Hệ mở", "B. Hệ kín", "C. Hệ cô lập", "D. Hệ dị thể"], "ans": "C"},
    {"q": "Câu 3. Hệ không trao đổi vật chất nhưng có trao đổi năng lượng với môi trường là?", "ops": ["A. Hệ cô lập", "B. Hệ kín", "C. Hệ mở", "D. Hệ đồng thể"], "ans": "B"},
    {"q": "Câu 4. Hệ có trao đổi cả vật chất và năng lượng với môi trường là?", "ops": ["A. Hệ cô lập", "B. Hệ kín", "C. Hệ mở", "D. Hệ dị thể"], "ans": "C"},
    {"q": "Câu 5. Hệ không có bề mặt phân chia thành các phần có tính chất hóa lý khác nhau gọi là?", "ops": ["A. Hệ dị thể", "B. Hệ đồng thể", "C. Hệ cô lập", "D. Hệ mở"], "ans": "B"},
    {"q": "Câu 6. Hệ gồm hai pha trở lên, các pha ngăn cách nhau bởi bề mặt phân chia được gọi là?", "ops": ["A. Hệ đồng thể", "B. Hệ đồng nhất", "C. Hệ dị thể", "D. Hệ kín"], "ans": "C"},
    {"q": "Câu 7. Thông số nào sau đây là thông số trạng thái?", "ops": ["A. Công A", "B. Nhiệt lượng Q", "C. Nhiệt độ T", "D. Nhiệt lượng q"], "ans": "C"},
    {"q": "Câu 8. Thông số nào sau đây là thông số quá trình?", "ops": ["A. Nhiệt độ T", "B. Áp suất P", "C. Nhiệt lượng Q", "D. Nội năng U"], "ans": "C"},
    {"q": "Câu 9. Thông số cường độ là thông số?", "ops": ["A. Phụ thuộc vào lượng chất", "B. Không phụ thuộc vào lượng chất", "C. Chỉ có ở hệ mở", "D. Chỉ có ở hệ cô lập"], "ans": "B"},
    {"q": "Câu 10. Thông số khuếch độ là thông số?", "ops": ["A. Không phụ thuộc lượng chất", "B. Phụ thuộc vào lượng chất", "C. Chỉ tồn tại ở trạng thái cân bằng", "D. Không tồn tại trong hệ sống"], "ans": "B"},
    {"q": "Câu 11. Nguyên lý số 0 của nhiệt động học phát biểu về?", "ops": ["A. Bảo toàn năng lượng", "B. Cân bằng nhiệt", "C. Chiều hướng quá trình", "D. Entropy"], "ans": "B"},
    {"q": "Câu 12. Theo nguyên lý số 1, nhiệt lượng Q mà hệ nhận được bằng?", "ops": ["A. Công A trừ nội năng U", "B. Công A cộng biến đổi nội năng U", "C. Entropy S nhân nhiệt độ T", "D. Không liên quan đến công và nội năng"], "ans": "B"},
    {"q": "Câu 13. Công thức của nguyên lý 1 đối với hệ kín là?", "ops": ["A. ΔQ = ΔA − ΔU", "B. ΔQ = ΔA + ΔU", "C. ΔU = ΔQ × ΔA", "D. ΔA = ΔQ × ΔU"], "ans": "B"},
    {"q": "Câu 14. Khi ΔQ > 0 nghĩa là?", "ops": ["A. Hệ tỏa nhiệt", "B. Hệ thu nhiệt", "C. Hệ sinh công", "D. Hệ nhận công"], "ans": "B"},
    {"q": "Câu 15. Định luật Hexo là hệ quả của?", "ops": ["A. Nguyên lý số 0", "B. Nguyên lý số 1", "C. Nguyên lý số 2", "D. Định luật Carnot"], "ans": "B"},
    {"q": "Câu 16. Theo định luật Hexo, hiệu ứng nhiệt của một phản ứng phụ thuộc vào?", "ops": ["A. Cách biến chuyển của phản ứng", "B. Trạng thái chất đầu và chất cuối", "C. Thời gian phản ứng", "D. Tốc độ phản ứng"], "ans": "B"},
    {"q": "Câu 17. Có bao nhiêu dạng công cơ bản trong cơ thể sống?", "ops": ["A. 2", "B. 3", "C. 4", "D. 5"], "ans": "C"},
    {"q": "Câu 18. Công sinh ra khi tổng hợp các đại phân tử được gọi là?", "ops": ["A. Công cơ học", "B. Công hóa học", "C. Công thẩm thấu", "D. Công điện"], "ans": "B"},
    {"q": "Câu 19. Công vận chuyển các chất qua màng tế bào được gọi là?", "ops": ["A. Công hóa học", "B. Công cơ học", "C. Công thẩm thấu", "D. Công điện"], "ans": "C"},
    {"q": "Câu 20. Công vận chuyển các hạt mang điện được gọi là?", "ops": ["A. Công hóa học", "B. Công điện", "C. Công cơ học", "D. Công thẩm thấu"], "ans": "B"},
    {"q": "Câu 21. Thiết bị dùng để đo nhiệt lượng tỏa ra khi đốt cháy một mẫu chất là?", "ops": ["A. Nhiệt kế", "B. Bom nhiệt lượng", "C. Áp kế", "D. Calorimet gián tiếp"], "ans": "B"},
    {"q": "Câu 22. Động cơ nhiệt cần tiếp xúc với bao nhiêu nguồn nhiệt?", "ops": ["A. 1", "B. 2", "C. 3", "D. 4"], "ans": "B"},
    {"q": "Câu 23. Nguyên lý số 2 của nhiệt động học cho biết?", "ops": ["A. Bản chất của phản ứng", "B. Chiều hướng tự diễn biến của quá trình", "C. Cấu trúc phân tử", "D. Khối lượng của hệ"], "ans": "B"},
    {"q": "Câu 24. Gradient của một tham số là?", "ops": ["A. Tổng giá trị tham số ở hai điểm", "B. Hiệu giá trị tham số ở hai điểm chia cho khoảng cách giữa hai điểm", "C. Tích giá trị tham số ở hai điểm", "D. Giá trị trung bình của tham số"], "ans": "B"},
    {"q": "Câu 25. Entropy là đại lượng đặc trưng cho?", "ops": ["A. Khả năng sinh công", "B. Sự phân tán năng lượng", "C. Khối lượng của hệ", "D. Nhiệt độ của hệ"], "ans": "B"},
    {"q": "Câu 26. Theo định nghĩa 1, entropy được tính bằng công thức?", "ops": ["A. S = Q × T", "B. S = Q/T", "C. S = T/Q", "D. S = Q + T"], "ans": "B"},
    {"q": "Câu 27. Theo định nghĩa 2, công thức tính entropy là?", "ops": ["A. S = k.lnω", "B. S = k/ω", "C. S = k × ω", "D. S = ω/k"], "ans": "A"},
    {"q": "Câu 28. Trong công thức S = k.lnω, ω là?", "ops": ["A. Hằng số Boltzmann", "B. Xác suất nhiệt động", "C. Nhiệt độ tuyệt đối", "D. Nội năng"], "ans": "B"},
    {"q": "Câu 29. Trong quá trình đoạn nhiệt thuận nghịch, biến thiên entropy ΔS bằng?", "ops": ["A. 0", "B. Dương", "C. Âm", "D. Vô cực"], "ans": "A"},
    {"q": "Câu 30. Trong quá trình bất thuận nghịch, biến thiên entropy luôn?", "ops": ["A. Bằng 0", "B. Nhỏ hơn 0", "C. Lớn hơn 0", "D. Không xác định"], "ans": "C"},
    {"q": "Câu 31. Entanpi H được định nghĩa bởi công thức?", "ops": ["A. H = U − pV", "B. H = U + pV", "C. H = U × pV", "D. H = U/pV"], "ans": "B"},
    {"q": "Câu 32. Năng lượng tự do Helmholtz F được định nghĩa là?", "ops": ["A. F = U − TS", "B. F = U + TS", "C. F = U × TS", "D. F = H − TS"], "ans": "A"},
    {"q": "Câu 33. Thế nhiệt động Gibbs G được tính bằng?", "ops": ["A. G = U − TS", "B. G = H − TS", "C. G = F − pV", "D. G = U + TS"], "ans": "B"},
    {"q": "Câu 34. Phương trình trạng thái khí lý tưởng Mendeleev-Clapeyron là?", "ops": ["A. pV = nRT", "B. pT = nRV", "C. VT = nRp", "D. pVT = nR"], "ans": "A"},
    {"q": "Câu 35. Giá trị hằng số khí lý tưởng R trong hệ SI là?", "ops": ["A. 8,314 J/mol.K", "B. 22,4 J/mol.K", "C. 6,02 J/mol.K", "D. 1,987 J/mol.K"], "ans": "A"},
    {"q": "Câu 36. Nội năng U của khí lý tưởng được tính bằng?", "ops": ["A. U = nRT", "B. U = (3/2)nRT", "C. U = (1/2)nRT", "D. U = 2nRT"], "ans": "B"},
    {"q": "Câu 37. Nội năng của hệ không bao gồm?", "ops": ["A. Năng lượng chuyển động phân tử", "B. Thế năng trọng trường và động năng tập thể của hệ", "C. Năng lượng liên kết hạt nhân", "D. Năng lượng dao động phân tử"], "ans": "B"},
    {"q": "Câu 38. Quá trình giữ áp suất không đổi được gọi là?", "ops": ["A. Đẳng nhiệt", "B. Đẳng áp", "C. Đẳng tích", "D. Đoạn nhiệt"], "ans": "B"},
    {"q": "Câu 39. Quá trình không có sự trao đổi nhiệt với môi trường được gọi là?", "ops": ["A. Đẳng áp", "B. Đẳng tích", "C. Đoạn nhiệt", "D. Đẳng nhiệt"], "ans": "C"},
    {"q": "Câu 40. Quá trình có thể tự trở về trạng thái ban đầu mà không cần năng lượng bên ngoài gọi là?", "ops": ["A. Quá trình bất thuận nghịch", "B. Quá trình thuận nghịch", "C. Quá trình đoạn nhiệt", "D. Quá trình đẳng áp"], "ans": "B"},
    {"q": "Câu 41. Vì sao các quá trình hóa sinh và lý sinh trong cơ thể sống đều là quá trình bất thuận nghịch?", "ops": ["A. Vì chúng luôn cần cung cấp năng lượng để trở về trạng thái ban đầu", "B. Vì chúng luôn xảy ra ở nhiệt độ không đổi", "C. Vì chúng không tiêu tốn năng lượng", "D. Vì chúng luôn ở trạng thái cân bằng"], "ans": "A"},
    {"q": "Câu 42. Trong hệ kín, tại trạng thái cân bằng nhiệt động thì?", "ops": ["A. dU vẫn thay đổi liên tục", "B. dU = 0", "C. dS < 0", "D. Hệ vẫn tiếp tục sinh công"], "ans": "B"},
    {"q": "Câu 43. Ở trạng thái cân bằng nhiệt động, năng lượng tự do F/G của hệ có xu hướng?", "ops": ["A. Đạt giá trị cực đại", "B. Đạt giá trị cực tiểu (min), hệ không còn khả năng sinh công", "C. Không đổi và bằng 0 luôn", "D. Tăng liên tục theo thời gian"], "ans": "B"},
    {"q": "Câu 44. So với cân bằng nhiệt động, trạng thái cân bằng dừng của hệ sống khác biệt chủ yếu ở điểm nào?", "ops": ["A. Là hệ cô lập, không trao đổi gì với môi trường", "B. Là hệ mở, luôn có dòng vật chất/năng lượng ra vào, tồn tại gradient", "C. Không có entropy", "D. Không tuân theo nguyên lý 1"], "ans": "B"},
    {"q": "Câu 45. Tại trạng thái cân bằng dừng, entropy của hệ sống có đặc điểm gì?", "ops": ["A. Đạt cực đại (Smax)", "B. Bằng 0", "C. Khác 0, là hằng số và nhỏ hơn Smax", "D. Luôn tăng vô hạn"], "ans": "C"},
    {"q": "Câu 46. Công thức Prigogine dS/dt = dSe/dt + dSi/dt bằng 0 khi nào?", "ops": ["A. Hệ đạt trạng thái cân bằng dừng", "B. Hệ đạt cân bằng nhiệt động", "C. Hệ đang sinh công tối đa", "D. Hệ bị cô lập hoàn toàn"], "ans": "A"},
    {"q": "Câu 47. Trong công thức dS = dSi + dSe, dSi luôn có tính chất?", "ops": ["A. Có thể âm", "B. Luôn dương (dSi > 0)", "C. Luôn bằng 0", "D. Luôn bằng dSe"], "ans": "B"},
    {"q": "Câu 48. dSe trong công thức Prigogine có thể mang giá trị như thế nào?", "ops": ["A. Chỉ dương", "B. Chỉ âm", "C. Chỉ bằng 0", "D. Có thể dương, âm hoặc bằng 0"], "ans": "D"},
    {"q": "Câu 49. Vì sao hệ thống sống có thể duy trì trật tự cao mặc dù nguyên lý 2 cho rằng entropy có xu hướng tăng?", "ops": ["A. Vì hệ sống là hệ cô lập", "B. Vì hệ sống là hệ mở, có thể giảm entropy nội tại nhờ trao đổi vật chất/năng lượng với môi trường (dSe âm)", "C. Vì hệ sống không tuân theo nguyên lý 2", "D. Vì hệ sống không có entropy"], "ans": "B"},
    {"q": "Câu 50. Hiệu suất động cơ nhiệt theo chu trình Carnot được tính bằng công thức nào?", "ops": ["A. η = T1/T2", "B. η = (T1−T2)/T1", "C. η = (T2−T1)/T2", "D. η = T1 × T2"], "ans": "B"},
    {"q": "Câu 51. Theo chu trình Carnot, hiệu suất máy nhiệt phụ thuộc vào?", "ops": ["A. Bản chất vật liệu chế tạo máy", "B. Nhiệt độ nguồn nóng và nguồn lạnh", "C. Khối lượng của máy", "D. Thời gian hoạt động"], "ans": "B"},
    {"q": "Câu 52. Vì sao hiệu suất động cơ nhiệt η luôn nhỏ hơn 1?", "ops": ["A. Vì công luôn lớn hơn nhiệt lượng cấp vào", "B. Vì một phần nhiệt luôn phải nhường cho nguồn lạnh, không thể biến đổi hoàn toàn thành công", "C. Vì nhiệt độ T2 luôn âm", "D. Vì máy luôn bị hao mòn"], "ans": "B"},
    {"q": "Câu 53. Phát biểu \"máy lạnh lý tưởng không tồn tại\" là hệ quả của?", "ops": ["A. Nguyen lý số 0", "B. Nguyên lý số 1", "C. Định luật 2 dạng 2 (nhiệt không tự truyền từ vật lạnh sang vật nóng hơn)", "D. Định luật Hexo"], "ans": "C"},
    {"q": "Câu 54. Trong công thức ΔQ = ΔA + ΔE + ΔM áp dụng cho cơ thể sống, ΔM đại diện cho?", "ops": ["A. Công cơ thể thực hiện", "B. Năng lượng mất mát ra môi trường", "C. Năng lượng dự trữ dưới dạng hóa năng", "D. Nhiệt lượng sinh ra khi đốt thức ăn"], "ans": "C"},
    {"q": "Câu 55. Nhiệt lượng sơ cấp trong cơ thể sống sinh ra do?", "ops": ["A. Đứt các liên kết giàu năng lượng ATP", "B. Phân tán năng lượng trong quá trình trao đổi vật chất (các phản ứng hóa sinh không thuận nghịch)", "C. Co cơ", "D. Hô hấp ngoài"], "ans": "B"},
    {"q": "Câu 56. Nhiệt lượng thứ cấp trong cơ thể sống sinh ra khi nào?", "ops": ["A. Khi tổng hợp glycogen", "B. Khi đứt các liên kết giàu năng lượng (ATP) để điều hòa hoạt động chủ động của cơ thể", "C. Khi hình thành liên kết peptit", "D. Khi hấp thu oxy"], "ans": "B"},
    {"q": "Câu 57. Ở điều kiện thông thường, nhiệt lượng sơ cấp và thứ cấp trong cơ thể có mối quan hệ như thế nào?", "ops": ["A. Luôn triệt tiêu lẫn nhau bằng 0", "B. Cân bằng với nhau", "C. Sơ cấp luôn lớn hơn thứ cấp rất nhiều", "D. Không liên quan gì đến nhau"], "ans": "B"},
    {"q": "Câu 58. Công thực hiện khi co cơ được tính gần đúng theo công thức nào?", "ops": ["A. A = ∫F(x)dx, Amax ≈ 0,45 Fmax×Δxmax", "B. A = pΔV", "C. A = QΔT", "D. A = mgh"], "ans": "A"},
    {"q": "Câu 59. Công trong quá trình hô hấp được tính bằng công thức nào?", "ops": ["A. A = ∫pdV", "B. A = ∫Fdx", "C. A = QT", "D. A = ΔU"], "ans": "A"},
    {"q": "Câu 60. Trong tuần hoàn, công A của tim được xác định chủ yếu bởi những yếu tố nào?", "ops": ["A. Nhiệt độ và thể tích máu", "B. Áp suất P đẩy máu và độ căng cơ (trương lực cơ)", "C. Nồng độ oxy trong máu", "D. Khối lượng cơ tim"], "ans": "B"},
    {"q": "Câu 61. ATP có thể được tổng hợp từ phản ứng nào sau đây?", "ops": ["A. Glucose + O2 → CO2 + H2O", "B. Photphocreatin + ADP → ATP + creatin", "C. Protein + nước → axit amin", "D. Lipid + O2 → CO2 + H2O + năng lượng"], "ans": "B"},
    {"q": "Câu 62. Phản ứng phân hủy glycogen giải phóng ATP có dạng?", "ops": ["A. Glucose + 3H3PO4 → 2 Lactat + 2ATP + 2H2O", "B. ATP → ADP + Pi", "C. Creatin + ATP → photphocreatin", "D. Glucose + O2 → 6CO2 + 6H2O"], "ans": "A"},
    {"q": "Câu 63. Phương pháp nhiệt lượng kế gián tiếp của La Voizier và Laplace dựa trên nguyên tắc nào?", "ops": ["A. Đo trực tiếp nhiệt độ cơ thể", "B. Khi không sinh công ngoài, nhiệt do cơ thể sinh ra xấp xỉ nhiệt sinh ra khi đốt cháy hoàn toàn thức ăn thành CO2 và H2O", "C. Đo lượng oxy tiêu thụ", "D. Đo khối lượng cơ thể trước và sau ăn"], "ans": "B"},
    {"q": "Câu 64. Tại sao entropy được xem là \"độ đo sự phân tán năng lượng\"?", "ops": ["A. Vì entropy luôn giảm theo thời gian", "B. Vì entropy tăng lên khi năng lượng trở nên kém tập trung, kém khả năng sinh công hơn", "C. Vì entropy tỉ lệ nghịch với nhiệt độ", "D. Vì entropy không liên quan đến năng lượng"], "ans": "B"},
    {"q": "Câu 65. Trạng thái có entropy lớn là trạng thái?", "ops": ["A. Khó xảy ra nhất, xác suất thấp nhất", "B. Dễ xảy ra nhất, có xác suất xảy ra lớn nhất", "C. Không thể xảy ra", "D. Chỉ xảy ra ở nhiệt độ 0K"], "ans": "B"},
    {"q": "Câu 66. Vì sao nói entropy là \"hàm trạng thái\"?", "ops": ["A. Vì giá trị của nó chỉ phụ thuộc vào cách biến đổi", "B. Vì giá trị biến thiên của nó chỉ phụ thuộc trạng thái đầu và cuối, không phụ thuộc con đường biến đổi", "C. Vì nó luôn không đổi", "D. Vì nó chỉ áp dụng cho hệ cô lập"], "ans": "B"},
    {"q": "Câu 67. Công thức nào biểu diễn điều kiện tự diễn biến của phản ứng ở điều kiện đẳng nhiệt, đẳng áp?", "ops": ["A. ΔG > 0", "B. ΔG = 0", "C. (dG)T,P < 0", "D. ΔS < 0"], "ans": "C"},
    {"q": "Câu 68. Biểu thức ΔG = ΔH − TΔS cho biết điều gì?", "ops": ["A. Mối liên hệ giữa năng lượng tự do Gibbs với entanpi và entropy", "B. Công thức tính nội năng", "C. Định luật bảo toàn khối lượng", "D. Phương trình trạng thái khí lý tưởng"], "ans": "A"},
    {"q": "Câu 69. Trong điều kiện thể tích không đổi (V=const), hệ tự phát biến đổi khi nào?", "ops": ["A. dU − TdS > 0", "B. dU − TdS < 0", "C. dU = TdS", "D. dS = 0"], "ans": "B"},
    {"q": "Câu 70. Trong điều kiện áp suất không đổi (P=const), điều kiện hệ tự phát biến đổi là?", "ops": ["A. dS > dH/T", "B. dS < dH/T", "C. dH = 0", "D. dS = 0"], "ans": "A"},
    {"q": "Câu 71. Đại lượng nào sau đây KHÔNG phải là hàm trạng thái?", "ops": ["A. Nội năng U", "B. Entanpi H", "C. Nhiệt lượng Q", "D. Entropy S"], "ans": "C"},
    {"q": "Câu 72. Ý nghĩa của gradient nồng độ dC/dx trong tế bào sống là gì?", "ops": ["A. Không có ý nghĩa sinh học", "B. Sự tồn tại của gradient tạo ra khả năng thực hiện công của tế bào sống", "C. Chỉ có ý nghĩa vật lý, không liên quan sinh học", "D. Luôn bằng 0 trong tế bào sống"], "ans": "B"},
    {"q": "Câu 73. Sự khác biệt cơ bản giữa quá trình đẳng nhiệt và đoạn nhiệt là gì?", "ops": ["A. Đẳng nhiệt không trao đổi nhiệt còn đoạn nhiệt có trao đổi nhiệt", "B. Đẳng nhiệt giữ T không đổi (có thể trao đổi nhiệt khi V/P thay đổi), đoạn nhiệt không trao đổi nhiệt (T có thể thay đổi)", "C. Cả hai đều không trao đổi nhiệt", "D. Cả hai đều giữ nhiệt độ không đổi"], "ans": "B"},
    {"q": "Câu 74. Vì sao trong quá trình đẳng nhiệt vẫn có thể xảy ra trao đổi nhiệt với môi trường?", "ops": ["A. Vì nhiệt độ không thực sự cố định", "B. Để bù lại sự thay đổi thể tích/áp suất mà vẫn giữ nhiệt độ không đổi", "C. Vì đẳng nhiệt luôn đi kèm với đoạn nhiệt", "D. Vì đó là do sai số đo lường"], "ans": "B"},
    {"q": "Câu 75. Bốn dạng công cơ bản trong cơ thể sống đều cần loại năng lượng chủ yếu nào để thực hiện?", "ops": ["A. Nhiệt năng", "B. ATP, GTP", "C. Quang năng", "D. Cơ năng từ bên ngoài"], "ans": "B"},
    {"q": "Câu 76. Một hệ kín nhận nhiệt lượng Q = 500 J và sinh công A = 200 J. Độ biến thiên nội năng ΔU của hệ là?", "ops": ["A. 300 J", "B. 700 J", "C. −300 J", "D. −700 J"], "ans": "A"},
    {"q": "Câu 77. Một động cơ nhiệt hoạt động giữa nguồn nóng T1 = 600 K và nguồn lạnh T2 = 300 K. Hiệu suất lý tưởng của động cơ là?", "ops": ["A. 25%", "B. 50%", "C. 75%", "D. 100%"], "ans": "B"},
    {"q": "Câu 78. Một khối khí lý tưởng có n = 2 mol ở nhiệt độ T = 300 K (R = 8,314 J/mol.K). Nội năng của khối khí xấp xỉ bằng bao nhiêu?", "ops": ["A. 7,48 kJ", "B. 3,74 kJ", "C. 14,96 kJ", "D. 2,49 kJ"], "ans": "A"},
    {"q": "Câu 79. Xét quá trình đẳng nhiệt thuận nghịch nhận nhiệt lượng Q = 1000 J ở nhiệt độ T = 250 K. Biến thiên entropy ΔS là?", "ops": ["A. 4 J/K", "B. 0,25 J/K", "C. 250 J/K", "D. 1000 J/K"], "ans": "A"},
    {"q": "Câu 80. Một phản ứng có ΔH = −50 kJ, ΔS = −100 J/K, ở T = 300 K. Giá trị ΔG là?", "ops": ["A. −20 kJ", "B. −80 kJ", "C. 20 kJ", "D. 80 kJ"], "ans": "A"},
    {"q": "Câu 81. Với dữ liệu ΔG = −20 kJ (< 0) ở câu trên, có thể kết luận gì về phản ứng?", "ops": ["A. Phản ứng không tự diễn biến", "B. Phản ứng tự diễn biến ở điều kiện đó", "C. Phản ứng đang ở trạng thái cân bằng", "D. Không đủ dữ liệu để kết luận"], "ans": "B"},
    {"q": "Câu 82. Nếu ΔH > 0 và ΔS > 0 trong một phản ứng, phản ứng có tự diễn biến hay không phụ thuộc vào?", "ops": ["A. Không bao giờ tự diễn biến", "B. Luôn tự diễn biến ở mọi nhiệt độ", "C. Tự diễn biến khi nhiệt độ đủ cao (T lớn để TΔS > ΔH)", "D. Không phụ thuộc nhiệt độ"], "ans": "C"},
    {"q": "Câu 83. Nếu ΔH < 0 và ΔS < 0, phản ứng tự diễn biến khi nào?", "ops": ["A. Ở nhiệt độ thấp (khi |ΔH| > |TΔS|)", "B. Ở nhiệt độ cao", "C. Không bao giờ tự diễn biến", "D. Luôn tự diễn biến bất kể nhiệt độ"], "ans": "A"},
    {"q": "Câu 84. Xác suất nhiệt động ω của một hệ tăng lên 10 lần. Biến thiên entropy ΔS (theo hằng số Boltzmann k) là bao nhiêu?", "ops": ["A. k.ln(10) ≈ 2,303k", "B. 10k", "C. k/10", "D. k.ln(0,1)"], "ans": "A"},
    {"q": "Câu 85. Một hệ cô lập luôn có đặc điểm gì về entropy theo thời gian?", "ops": ["A. Luôn giảm", "B. Luôn không đổi", "C. Luôn tăng hoặc không đổi (dS ≥ 0), tiến tới cực đại khi cân bằng", "D. Dao động không xác định"], "ans": "C"},
    {"q": "Câu 86. So sánh quá trình thuận nghịch và bất thuận nghịch về biến thiên entropy tổng cộng (hệ + môi trường)?", "ops": ["A. Thuận nghịch: ΔS tổng = 0; bất thuận nghịch: ΔS tổng > 0", "B. Cả hai đều có ΔS tổng = 0", "C. Cả hai đều có ΔS tổng > 0", "D. Không thể so sánh"], "ans": "A"},
    {"q": "Câu 87. Tại sao \"công có thể biến đổi hoàn toàn thành nhiệt nhưng nhiệt không thể biến đổi hoàn toàn thành công\"?", "ops": ["A. Vì công là dạng năng lượng có trật tự cao (chuyển động định hướng), còn nhiệt là chuyển động hỗn loạn của phân tử, nên chuyển ngược lại luôn có hao phí", "B. Vì nhiệt luôn lớn hơn công về giá trị tuyệt đối", "C. Vì đó chỉ là một quy ước tính toán", "D. Vì công luôn bằng 0"], "ans": "A"},
    {"q": "Câu 88. Một tế bào duy trì cấu trúc trật tự cao (entropy nội tại cục bộ có xu hướng giảm). Điều này có mâu thuẫn với nguyên lý 2 không?", "ops": ["A. Có mâu thuẫn vì entropy hệ cô lập luôn phải tăng", "B. Không mâu thuẫn, vì tế bào là hệ mở: dSe đủ âm bù cho dSi > 0 cục bộ, còn xét toàn hệ mở rộng (tế bào + môi trường) entropy tổng vẫn tăng", "C. Không mâu thuẫn vì tế bào không tuân theo các định luật vật lý", "D. Có mâu thuẫn nên nguyên lý 2 không áp dụng cho sinh vật"], "ans": "B"},
    {"q": "Câu 89. Trạng thái cân bằng dừng khác trạng thái cân bằng nhiệt động ở điểm mấu chốt nào liên quan đến khả năng sinh công?", "ops": ["A. Cả hai đều không có khả năng sinh công", "B. Cân bằng dừng có G, F khác 0 (const) nên hệ vẫn có khả năng sinh công; cân bằng nhiệt động có G, F → min nên hết khả năng sinh công", "C. Cân bằng nhiệt động luôn sinh công lớn hơn", "D. Không có sự khác biệt nào"], "ans": "B"},
    {"q": "Câu 90. Vì sao cơ thể sống được xem là \"hệ mở đặc biệt\" hơn là một hệ mở thông thường?", "ops": ["A. Vì nó luôn đạt cân bằng nhiệt động thực sự", "B. Vì nó liên tục trao đổi vật chất/năng lượng với môi trường để duy trì trạng thái dừng có trật tự cao, chứ không tiến tới cân bằng nhiệt động (chết)", "C. Vì nó không tuân theo nguyên lý bảo toàn năng lượng", "D. Vì nó không có entropy"], "ans": "B"},
    {"q": "Câu 91. Nếu một cơ thể sống ngừng trao đổi chất với môi trường (chết), hệ sẽ tiến dần tới?", "ops": ["A. Trạng thái cân bằng dừng bền vững hơn", "B. Trạng thái cân bằng nhiệt động (entropy tiến tới cực đại, mất khả năng sinh công)", "C. Trạng thái entropy giảm dần về 0", "D. Không có sự thay đổi nào"], "ans": "B"},
    {"q": "Câu 92. Trong công thức ΔQ = ΔA + ΔE + ΔM, nếu cơ thể không thực hiện công ra bên ngoài (ΔA = 0) và không tích lũy năng lượng dự trữ (ΔM = 0), thì ΔQ xấp xỉ bằng?", "ops": ["A. 0", "B. ΔE (toàn bộ nhiệt sinh ra mất vào môi trường)", "C. ΔA", "D. Vô cực"], "ans": "B"},
    {"q": "Xét chu trình Carnot, nếu T1 (nguồn nóng) tăng lên trong khi T2 (nguồn lạnh) không đổi, hiệu suất η sẽ?", "ops": ["A. Giảm", "B. Tăng", "C. Không đổi", "D. Bằng 1"], "ans": "B"},
    {"q": "Nếu T2 (nguồn lạnh) tiến gần đến T1 (nguồn nóng), hiệu suất động cơ nhiệt η sẽ tiến gần đến?", "ops": ["A. 1", "B. 0", "C. Vô cực", "D. Âm"], "ans": "B"},
    {"q": "Một phản ứng có ΔH = −20 kJ, ΔS = +50 J/K. Ở mọi nhiệt độ dương, dấu của ΔG sẽ?", "ops": ["A. Luôn dương (không tự diễn biến)", "B. Luôn âm (luôn tự diễn biến ở mọi T > 0)", "C. Luôn bằng 0", "D. Phụ thuộc hoàn toàn vào áp suất"], "ans": "B"},
    {"q": "Một phản ứng có ΔH > 0, ΔS < 0. Dấu của ΔG ở mọi nhiệt độ dương sẽ?", "ops": ["A. Luôn âm", "B. Luôn dương (không bao giờ tự diễn biến)", "C. Bằng 0", "D. Phụ thuộc vào áp suất"], "ans": "B"},
    {"q": "Trong thí nghiệm bom nhiệt lượng, mẫu chất được đốt cháy trong điều kiện nào?", "ops": ["A. Hệ mở, áp suất khí quyển", "B. Hệ cô lập (kín, thể tích không đổi) để đo chính xác nhiệt tỏa ra", "C. Hệ có trao đổi vật chất tự do", "D. Điều kiện chân không tuyệt đối không có oxy"], "ans": "B"},
    {"q": "Tại sao phương pháp nhiệt lượng kế gián tiếp lại được gọi là \"gián tiếp\"?", "ops": ["A. Vì đo trực tiếp nhiệt lượng cơ thể tỏa ra bằng bom nhiệt lượng chứa cả cơ thể", "B. Vì suy ra nhiệt lượng cơ thể sinh ra thông qua nhiệt lượng đo được khi đốt cháy thức ăn (thành phần dinh dưỡng) trong bom nhiệt lượng, không đo trực tiếp trên cơ thể sống", "C. Vì không liên quan đến nhiệt lượng", "D. Vì đo qua nhiệt độ môi trường xung quanh"], "ans": "B"},
    {"q": "Nhận định nào sau đây về mối quan hệ giữa 3 nguyên lý nhiệt động học là đúng?", "ops": ["A. Nguyên lý 0 xác định chiều quá trình, nguyên lý 1 nói về cân bằng nhiệt, nguyên lý 2 bảo toàn năng lượng", "B. Nguyên lý 0 nói về cân bằng nhiệt, nguyên lý 1 là bảo toàn năng lượng, nguyên lý 2 xác định chiều hướng tự diễn biến", "C. Cả ba nguyên lý đều chỉ nói về entropy", "D. Cả ba nguyên lý đều tương đương nhau"], "ans": "B"},
    {"q": "Nhận định nào sau đây chính xác nhất khi so sánh vai trò của nguyên lý 1 và nguyên lý 2 trong nghiên cứu hệ sống?", "ops": ["A. Nguyên lý 1 cho biết năng lượng được bảo toàn/chuyển hóa (định lượng); nguyên lý 2 cho biết chiều hướng, khả năng và giới hạn tự diễn biến (định hướng); cả hai đều không cho biết cơ chế/bản chất chi tiết của quá trình", "B. Nguyên lý 1 và 2 hoàn toàn độc lập, không liên quan gì đến nhau trong hệ sống", "C. Nguyên lý 2 có thể thay thế hoàn toàn nguyên lý 1", "D. Chỉ nguyên lý 1 áp dụng được cho hệ sống, nguyên lý 2 không áp dụng được"], "ans": "A"}
]

# --- DỮ LIỆU PHẦN B: 25 CÂU HỎI ĐIỀN TỪ ---
fill_data = [
    {"q": "1. ______ là khoa học nghiên cứu về sự biến đổi năng lượng.", "ans": "Nhiệt động học"},
    {"q": "2. Hệ không trao đổi vật chất và năng lượng với môi trường xung quanh được gọi là hệ ______.", "ans": "cô lập"},
    {"q": "3. Hệ không trao đổi vật chất nhưng có trao đổi năng lượng với môi trường được gọi là hệ ______.", "ans": "kín", "alt": ["hệ đóng", "đóng"]},
    {"q": "4. Hệ có trao đổi cả vật chất và năng lượng với môi trường được gọi là hệ ______.", "ans": "mở"},
    {"q": "5. Hệ không có bề mặt phân chia thành các phần có tính chất hóa lý khác nhau được gọi là hệ ______.", "ans": "đồng thể"},
    {"q": "6. Hệ gồm hai pha trở lên, ngăn cách nhau bởi bề mặt phân chia, được gọi là hệ ______.", "ans": "dị thể"},
    {"q": "7. Nội năng là năng lượng ______ toàn phần của tất cả các dạng chuyển động và tương tác của các phần tử trong hệ.", "ans": "dự trữ"},
    {"q": "8. Theo nguyên lý số 1, nhiệt lượng Q mà hệ nhận được bằng công A mà hệ sinh ra cộng với sự biến đổi ______ của hệ.", "ans": "nội năng"},
    {"q": "9. Định luật ______ là hệ quả của nguyên lý số 1, cho biết hiệu ứng nhiệt chỉ phụ thuộc vào trạng thái đầu và cuối.", "ans": "Hexo"},
    {"q": "10. ______ là công cụ dùng để đo nhiệt lượng tỏa ra khi đốt cháy một mẫu chất trong điều kiện cô lập.", "ans": "Bom nhiệt lượng"},
    {"q": "11. Nguyên lý số ______ phát biểu: nếu hai hệ cân bằng nhiệt với một hệ thứ ba thì chúng cân bằng nhiệt với nhau.", "ans": "0", "alt": ["không"]},
    {"q": "12. Đại lượng đặc trưng cho mức độ hỗn loạn hay sự phân tán năng lượng của hệ được gọi là ______.", "ans": "entropy"},
    {"q": "13. Công thức S = k.lnω biểu diễn entropy theo định nghĩa ______ (mức độ hỗn loạn của hệ).", "ans": "thứ hai", "alt": ["2", "thứ 2"]},
    {"q": "14. Trong công thức S = k.lnω, ω được gọi là ______.", "ans": "xác suất nhiệt động"},
    {"q": "15. ______ là năng lượng có thể biến thành công hoàn toàn sau khi trừ đi phần năng lượng mất mát để tăng entropy.", "ans": "Năng lượng tự do"},
    {"q": "16. Ở điều kiện T, V không đổi, năng lượng tự do được gọi là năng lượng tự do ______.", "ans": "Helmholtz"},
    {"q": "17. Ở điều kiện T, P không đổi, năng lượng tự do được gọi là thế nhiệt động ______.", "ans": "Gibbs"},
    {"q": "18. ______ của một tham số là hiệu giá trị của tham số đó ở hai điểm, chia cho khoảng cách giữa hai điểm đó.", "ans": "Gradient"},
    {"q": "19. Quá trình có thể tự trở về trạng thái ban đầu mà không cần cung cấp năng lượng từ bên ngoài được gọi là quá trình ______.", "ans": "thuận nghịch"},
    {"q": "20. Quá trình không thể tự trở về trạng thái ban đầu nếu không được cung cấp năng lượng từ bên ngoài được gọi là quá trình ______.", "ans": "bất thuận nghịch"},
    {"q": "21. Theo định luật 2 dạng 2, ______ không thể tự truyền từ vật lạnh sang vật nóng hơn nếu không có sự thay đổi nào khác xảy ra.", "ans": "nhiệt lượng"},
    {"q": "22. Trạng thái mà các thông số của một hệ mở không đổi theo thời gian dù vẫn có dòng vật chất/năng lượng ra vào được gọi là trạng thái ______.", "ans": "cân bằng dừng"},
    {"q": "23. Bốn dạng công cơ bản trong cơ thể sống gồm: công hóa học, công cơ học, công thẩm thấu và công ______.", "ans": "điện"},
    {"q": "24. Phương trình pV = nRT được gọi là phương trình ______.", "ans": "Mendeleev-Clapeyron"},
    {"q": "25. Công thức Prigogine biểu diễn: dS/dt = dSe/dt + ______ /dt.", "ans": "dSi"}
]

# --- QUẢN LÝ TRẠNG THÁI LUỒNG CÂU HỎI ---
if 'answers_a' not in st.session_state:
    st.session_state.answers_a = [None] * len(quiz_data)
if 'answers_b' not in st.session_state:
    st.session_state.answers_b = [""] * len(fill_data)

# --- THIẾT KẾ MENU THANH BÊN ---
st.sidebar.title("📚 Lựa chọn phần ôn tập")
menu = st.sidebar.radio("Chuyển đổi nhanh:", ["Phần A: Trắc nghiệm (100 câu)", "Phần B: Điền từ (25 câu)"])

# --- GIAO DIỆN CHÍNH ---
st.title("🔥 ÔN TẬP TỰ ĐỘNG CHẤM CHƯƠNG 1")
st.caption("Nội dung tham chiếu cấu trúc tệp dữ liệu: 'Câu hỏi chương 2.docx'")
st.markdown("---")

# 1. LOGIC XỬ LÝ PHẦN TRẮC NGHIỆM
if menu == "Phần A: Trắc nghiệm (100 câu)":
    st.header("📝 PHẦN A. TRẮC NGHIỆM TỰ ĐỘNG CHẤM TỨC THÌ")
    
    def render_block(start_idx, end_idx, title):
        st.subheader(title)
        for i in range(start_idx, end_idx):
            item = quiz_data[i]
            saved_idx = st.session_state.answers_a[i]
            
            # Khởi tạo widget trắc nghiệm dạng hàng ngang (horizontal)
            user_choice = st.radio(
                item["q"], 
                item["ops"], 
                index=saved_idx, 
                key=f"mcq_{i}", 
                horizontal=True
            )
            
            if user_choice is not None:
                st.session_state.answers_a[i] = item["ops"].index(user_choice)
                
                # Kiểm tra ký tự đầu để chấm điểm tự động (Ví dụ: 'A' == 'A')
                if user_choice[0] == item["ans"]:
                    st.success(f"✅ Đúng! Đáp án đúng là: **{item['ans']}**")
                else:
                    st.error(f"❌ Chưa chính xác. Đáp án đúng là: **{item['ans']}**")
            st.markdown("<hr style='margin: 10px 0px; border-top: 1px dashed #bbb;'>", unsafe_allow_html=True)

    render_block(0, 40, "I. Mức độ Nhận biết (Câu 1 – 40)")
    render_block(40, 75, "II. Mức độ Thông hiểu (Câu 41 – 75)")
    render_block(75, 100, "III. Mức độ Vận dụng / Vận dụng cao (Câu 76 – 100)")

# 2. LOGIC XỬ LÝ PHẦN ĐIỀN TỪ
elif menu == "Phần B: Điền từ (25 câu)":
    st.header("✏️ PHẦN B. ĐIỀN TỪ CHẤM ĐIỂM KHI ẤN ENTER")
    st.info("Nhập câu trả lời ngắn của bạn rồi ấn phím **Enter** trên bàn phím để nhận kết quả[cite: 2].")
    
    for i, item in enumerate(fill_data):
        input_text = st.text_input(item["q"], value=st.session_state.answers_b[i], key=f"fld_{i}").strip()
        st.session_state.answers_b[i] = input_text
        
        if input_text != "":
            student_ans = input_text.lower()
            correct_ans = item["ans"].lower()
            
            # Kiểm tra so khớp đáp án chính xác hoặc cụm từ viết tắt/đồng nghĩa quy ước sẵn
            is_match = (student_ans == correct_ans)
            if "alt" in item:
                for alt_text in item["alt"]:
                    if student_ans == alt_text.lower():
                        is_match = True
                        
            if is_match:
                st.success(f"✅ Chính xác! Đáp án đúng: **{item['ans']}**")
            else:
                st.error(f"❌ Sai rồi. Đáp án chính xác là: **{item['ans']}**")
        st.write("")