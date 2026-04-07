# from manim import *
# import numpy as np

# # BẢNG MÀU TỔNG HỢP (Gộp từ cả 2 file)
# VN_FONT = "Arial"
# C_MAIN = BLUE_C      
# C_LAMBDA = YELLOW_C  
# C_VECTOR = GREEN_C   
# C_SVD = ORANGE       
# C_U = TEAL_C
# C_SIGMA = GOLD_C
# C_V = PURPLE_C

# # Thêm màu cho SVD Premium Geometry
# C_TITLE = WHITE
# C_MATH = WHITE
# C_VEC_1 = TEAL_C
# C_VEC_2 = RED_C
# C_GRID = BLUE_E

# # KÍCH THƯỚC CHỮ
# TITLE_SIZE = 32           
# SUBTITLE_SIZE = 26        
# FORMULA_MAIN_SIZE = 56    

# BODY_TEXT_SIZE = 24       
# BODY_MATH_SIZE = 36       

# NOTE_TEXT_SIZE = 20      
# NOTE_MATH_SIZE = 28      


# class Section1_IntroProblem(Scene):
#     def construct(self):
#         title = Text("PHÂN RÃ SVD VÀ CHÉO HÓA", font=VN_FONT, font_size=42, weight=BOLD)
#         title.to_edge(UP, buff=1.5)
        
#         subtitle = Text("Giới thiệu ma trận nghiên cứu:", font=VN_FONT, font_size=SUBTITLE_SIZE, color=LIGHT_GREY)
#         subtitle.next_to(title, DOWN, buff=1)

#         matrix_A = MathTex("A", "=", "\\begin{pmatrix} 1 & 2 \\\\ -1 & 4 \\end{pmatrix}", font_size=FORMULA_MAIN_SIZE)
#         matrix_A.next_to(subtitle, DOWN, buff=0.5)
#         matrix_A[0].set_color(C_MAIN)

#         self.play(Write(title))
#         self.play(FadeIn(subtitle, shift=DOWN))
#         self.play(Write(matrix_A))
#         self.play(Indicate(matrix_A[0], color=C_MAIN, scale_factor=1.2))
#         self.wait(2)

#         self.play(FadeOut(VGroup(title, subtitle, matrix_A)))


# class Section23_Theory_And_GeometricSVD(Scene):
#     def construct(self):
#         # Đổi màu nền Premium (sẽ áp dụng cho cả scene lý thuyết và hình học)
#         self.camera.background_color = "#0d1117"
        
#         self.show_theory()
#         self.show_geometry()

#     def show_theory(self):
#         # KHÔNG THAY ĐỔI: Phần lý thuyết đã được tối ưu typography từ trước
#         title = Text("2. Cơ sở lý thuyết phân rã SVD", font=VN_FONT, font_size=TITLE_SIZE, color=C_SVD).to_corner(UL)
#         self.play(FadeIn(title))

#         intro_text = Text("Dạng phân rã tổng quát cho ma trận bất kỳ:", font=VN_FONT, font_size=SUBTITLE_SIZE).shift(UP*2.2)
#         formula = MathTex("A", "=", "U", "\\Sigma", "V^T", font_size=FORMULA_MAIN_SIZE).next_to(intro_text, DOWN, buff=0.4)
#         formula[0].set_color(C_MAIN)
#         formula[2].set_color(C_U)
#         formula[3].set_color(C_SIGMA)
#         formula[4].set_color(C_V)

#         self.play(Write(intro_text), FadeIn(formula, shift=UP))
#         self.wait(1)

#         u_line = VGroup(
#             MathTex("U \\in \\mathbb{R}^{m \\times m}", font_size=BODY_MATH_SIZE, color=C_U),
#             Text(": Ma trận trực giao", font=VN_FONT, font_size=BODY_TEXT_SIZE),
#             MathTex("(U^T U = I)", font_size=BODY_MATH_SIZE)
#         ).arrange(RIGHT, buff=0.2)
#         u_sub = Text("Các cột là vector suy biến trái (left singular vectors)", font=VN_FONT, font_size=NOTE_TEXT_SIZE, color=LIGHT_GREY)
#         u_block = VGroup(u_line, u_sub).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

#         sigma_line = VGroup(
#             MathTex("\\Sigma \\in \\mathbb{R}^{m \\times n}", font_size=BODY_MATH_SIZE, color=C_SIGMA),
#             Text(": Ma trận đường chéo", font=VN_FONT, font_size=BODY_TEXT_SIZE),
#             MathTex("\\Sigma = \\text{diag}(\\sigma_1, \\dots, \\sigma_p)", font_size=BODY_MATH_SIZE)
#         ).arrange(RIGHT, buff=0.2)
        
#         sigma_sub = VGroup(
#             Text("Với", font=VN_FONT, font_size=NOTE_TEXT_SIZE, color=LIGHT_GREY),
#             MathTex("p = \\min(m, n)", font_size=NOTE_MATH_SIZE, color=LIGHT_GREY),
#             Text("và", font=VN_FONT, font_size=NOTE_TEXT_SIZE, color=LIGHT_GREY),
#             MathTex("\\sigma_1 \\ge \\sigma_2 \\ge \\dots \\ge \\sigma_p \\ge 0", font_size=NOTE_MATH_SIZE, color=LIGHT_GREY)
#         ).arrange(RIGHT, buff=0.15)
#         sigma_block = VGroup(sigma_line, sigma_sub).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

#         v_line = VGroup(
#             MathTex("V \\in \\mathbb{R}^{n \\times n}", font_size=BODY_MATH_SIZE, color=C_V),
#             Text(": Ma trận trực giao", font=VN_FONT, font_size=BODY_TEXT_SIZE),
#             MathTex("(V^T V = I)", font_size=BODY_MATH_SIZE)
#         ).arrange(RIGHT, buff=0.2)
#         v_sub = Text("Các cột là vector suy biến phải (right singular vectors)", font=VN_FONT, font_size=NOTE_TEXT_SIZE, color=LIGHT_GREY)
#         v_block = VGroup(v_line, v_sub).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

#         all_blocks = VGroup(u_block, sigma_block, v_block).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
#         all_blocks.next_to(formula, DOWN, buff=0.8).to_edge(LEFT, buff=1.5)

#         self.play(FadeIn(u_block, shift=RIGHT))
#         self.play(FadeIn(sigma_block, shift=RIGHT))
#         self.play(FadeIn(v_block, shift=RIGHT))
#         self.wait(3)

#         self.play(FadeOut(VGroup(title, intro_text, formula, all_blocks)))

#     def show_geometry(self):
#         # =========================================================
#         # [LAYOUT ENGINE] - ĐỊNH NGHĨA CÁC TỌA ĐỘ NEO (ANCHORS)
#         # =========================================================
#         # 1. Tọa độ Y (Các tầng dọc)
#         Y_HEADER = 3.2      # Tầng 1: Tiêu đề 
#         Y_LABEL  = 1.8      # Tầng 2a: Tên ma trận
#         Y_MATRIX = 0.4      # Tầng 2b: Ma trận số 
#         Y_GRID   = -2.2     # Tầng 3: Lưới tọa độ & Trực quan hóa

#         # 2. Tọa độ X (Các cột ngang / Panels)
#         X_LEFT   = -4.6     # Panel 1 (Đầu vào V)
#         X_MID    = 0.0      # Panel 2 (Biến đổi Sigma)
#         X_RIGHT  = 4.6      # Panel 3 (Đầu ra U)

#         # =========================================================
#         # TẦNG 1: HEADER (TIÊU ĐỀ & CÔNG THỨC SVD)
#         # =========================================================
#         title = Text("3. Ý nghĩa hình học của SVD", font=VN_FONT, font_size=TITLE_SIZE, color=C_SVD).to_corner(UL)
#         #self.play(FadeIn(title))

        
#         svd_eq = MathTex("A", "=", "U", "\\Sigma", "V^T", font_size=56)
#         svd_eq.set_color_by_tex("U", C_U)
#         svd_eq.set_color_by_tex("\\Sigma", C_SIGMA)
#         svd_eq.set_color_by_tex("V^T", C_V)
        
#         # [MINIMAL FIX]: Chỉ dịch công thức xuống Y = 2.6 (nằm an toàn giữa tiêu đề và các ma trận)
#         svd_eq.move_to([X_MID, 2.6, 0]) 
        
#         self.play(FadeIn(title, shift=DOWN*0.3), Write(svd_eq))

#         # =========================================================
#         # TRACKERS (THAM SỐ CHUYỂN ĐỘNG HÌNH HỌC)
#         # =========================================================
#         vt_theta_v = ValueTracker(0)       
#         vt_sigma_x = ValueTracker(1.0)     
#         vt_sigma_y = ValueTracker(1.0)
#         vt_theta_u = ValueTracker(0)       

#         def get_V():
#             t = vt_theta_v.get_value()
#             return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])

#         def get_Sigma():
#             return np.array([[vt_sigma_x.get_value(), 0], [0, vt_sigma_y.get_value()]])

#         def get_U():
#             t = vt_theta_u.get_value()
#             return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])

#         # =========================================================
#         # TẦNG 3: VISUALIZATION ROW (LƯỚI TỌA ĐỘ VÀ MŨI TÊN CHỈ DÒNG)
#         # =========================================================
#         plane_kwargs = {
#             "x_range": [-4, 4], "y_range": [-4, 4],
#             "x_length": 3.2, "y_length": 3.2, 
#             "background_line_style": {"stroke_color": C_GRID, "stroke_width": 1, "stroke_opacity": 0.5},
#             "axis_config": {"stroke_color": GREY, "stroke_width": 2}
#         }
        
#         plane_in  = NumberPlane(**plane_kwargs).move_to([X_LEFT, Y_GRID, 0])
#         plane_mid = NumberPlane(**plane_kwargs).move_to([X_MID, Y_GRID, 0])
#         plane_out = NumberPlane(**plane_kwargs).move_to([X_RIGHT, Y_GRID, 0])

#         self.play(
#             LaggedStart(Create(plane_in), Create(plane_mid), Create(plane_out), lag_ratio=0.3), 
#             run_time=2
#         )

#         arrow_1 = MathTex("\\Rightarrow", font_size=40).move_to([(X_LEFT + X_MID)/2, Y_GRID, 0])
#         arrow_2 = MathTex("\\Rightarrow", font_size=40).move_to([(X_MID + X_RIGHT)/2, Y_GRID, 0])
#         self.play(FadeIn(arrow_1), FadeIn(arrow_2))

#         # =========================================================
#         # TẦNG 2: MATRIX ROW (NHÃN & MA TRẬN)
#         # =========================================================
#         lbl_v   = MathTex("V^T", font_size=40, color=C_V).move_to([X_LEFT, Y_LABEL, 0])
#         lbl_sig = MathTex("\\Sigma", font_size=40, color=C_SIGMA).move_to([X_MID, Y_LABEL, 0])
#         lbl_u   = MathTex("U", font_size=40, color=C_U).move_to([X_RIGHT, Y_LABEL, 0])

#         matrix_kwargs = {
#             "element_to_mobject_config": {"num_decimal_places": 2, "font_size": 26},
#             "h_buff": 1.1, "v_buff": 0.6
#         }

#         mat_v_dec = always_redraw(lambda: DecimalMatrix(get_V(), **matrix_kwargs).set_color(C_V).move_to([X_LEFT, Y_MATRIX, 0]))
#         mat_sig_dec = always_redraw(lambda: DecimalMatrix(get_Sigma(), **matrix_kwargs).set_color(C_SIGMA).move_to([X_MID, Y_MATRIX, 0]))
#         mat_u_dec = always_redraw(lambda: DecimalMatrix(get_U(), **matrix_kwargs).set_color(C_U).move_to([X_RIGHT, Y_MATRIX, 0]))

#         self.play(
#             Write(lbl_v), Write(lbl_sig), Write(lbl_u),
#             Write(mat_v_dec), Write(mat_sig_dec), Write(mat_u_dec)
#         )

#         # =========================================================
#         # TẠO HÌNH HỌC (SHAPES VÀ VECTORS) TRONG TẦNG 3
#         # =========================================================
#         def get_dynamic_shape(mat_func, plane, color_fill):
#             def creator():
#                 mat = mat_func()
#                 v1_end = mat @ np.array([1, 0])
#                 v2_end = mat @ np.array([0, 1])

#                 shape = Circle(radius=1.0).set_stroke(color_fill, 2).set_fill(color_fill, 0.25)
#                 mat_3x3 = np.eye(3); mat_3x3[:2, :2] = mat
#                 shape.apply_matrix(mat_3x3)
#                 shape.move_to(plane.get_origin()) 

#                 v1 = Arrow(plane.get_origin(), plane.c2p(v1_end[0], v1_end[1]), buff=0, color=C_VEC_1, stroke_width=4, max_tip_length_to_length_ratio=0.15)
#                 v2 = Arrow(plane.get_origin(), plane.c2p(v2_end[0], v2_end[1]), buff=0, color=C_VEC_2, stroke_width=4, max_tip_length_to_length_ratio=0.15)
                
#                 return VGroup(shape, v1, v2)
#             return always_redraw(creator)

#         shape_in  = get_dynamic_shape(get_V, plane_in, C_V)
#         shape_mid = get_dynamic_shape(lambda: get_Sigma(), plane_mid, C_SIGMA)
#         shape_out = get_dynamic_shape(lambda: get_U() @ get_Sigma(), plane_out, C_U)

#         self.play(FadeIn(shape_in), FadeIn(shape_mid), FadeIn(shape_out))
#         self.wait(1)

#         # =========================================================
#         # PIPELINE ANIMATION (BIẾN ĐỔI SVD)
#         # =========================================================
#         def highlight_matrix(matrix_mob, color):
#             return SurroundingRectangle(matrix_mob, color=color, corner_radius=0.1, buff=0.1)

#         # --- Nhịp 1: Quay V^T ---
#         box_v = highlight_matrix(mat_v_dec, C_V)
#         self.play(Create(box_v))
#         self.play(vt_theta_v.animate.set_value(PI / 4), run_time=2.5, rate_func=smooth)
#         self.play(FadeOut(box_v))
#         self.wait(0.5)

#         # --- Nhịp 2: Co giãn Sigma ---
#         box_sig = highlight_matrix(mat_sig_dec, C_SIGMA)
#         self.play(Create(box_sig))
#         self.play(
#             vt_sigma_x.animate.set_value(1.8),
#             vt_sigma_y.animate.set_value(0.6),
#             run_time=3, rate_func=smooth
#         )
#         self.play(FadeOut(box_sig))
#         self.wait(0.5)

#         # --- Nhịp 3: Quay U ---
#         box_u = highlight_matrix(mat_u_dec, C_U)
#         self.play(Create(box_u))
#         self.play(vt_theta_u.animate.set_value(PI / 6), run_time=2.5, rate_func=smooth)
#         self.play(FadeOut(box_u))
#         self.wait(1)

#         # --- Nhịp 4: Biến đổi tổng hợp ---
#         self.play(
#             vt_theta_v.animate.set_value(-PI / 3),
#             vt_sigma_x.animate.set_value(1.2),
#             vt_sigma_y.animate.set_value(1.8),
#             vt_theta_u.animate.set_value(-PI / 4),
#             run_time=4, rate_func=there_and_back 
#         )
#         self.wait(2)


# class MatrixDiagonalization(Scene):
#     def construct(self):
#         main_title = Text("4. Bài toán chéo hóa ma trận", font=VN_FONT, font_size=TITLE_SIZE, color=C_SVD).to_corner(UL)
#         self.play(FadeIn(main_title))

#         res_lambdas = self.step1_find_eigenvalues()
#         res_u1 = self.step2_find_eigenvector(
#             step_name="Tìm vector riêng cho",
#             lam_val="2",
#             mat_before="\\begin{pmatrix} 1-2 & 2 \\\\ -1 & 4-2 \\end{pmatrix}",
#             transform_op="d_2 - d_1", 
#             mat_after="\\begin{pmatrix} -1 & 2 \\\\ 0 & 0 \\end{pmatrix}",
#             eq_str="-x_1 + 2x_2 = 0",
#             vec_res="2 \\\\ 1",
#             u_subscript="1", 
#             ref_pos_shift=ORIGIN,
#             anchor=res_lambdas
#         )
#         res_u2 = self.step2_find_eigenvector(
#             step_name="Tìm vector riêng cho",
#             lam_val="3",
#             mat_before="\\begin{pmatrix} 1-3 & 2 \\\\ -1 & 4-3 \\end{pmatrix}",
#             transform_op="2d_2 - d_1", 
#             mat_after="\\begin{pmatrix} -2 & 2 \\\\ 0 & 0 \\end{pmatrix}",
#             eq_str="-2x_1 + 2x_2 = 0 \\Rightarrow -x_1 + x_2 = 0",
#             vec_res="1 \\\\ 1",
#             u_subscript="2", 
#             ref_pos_shift=DOWN*1.2,
#             anchor=res_lambdas
#         )
#         self.step3_build_matrices(res_u1, res_u2)

#     def step1_find_eigenvalues(self):
#         step_title = Text("Tìm đa thức đặc trưng và trị riêng", font=VN_FONT, font_size=BODY_TEXT_SIZE, color=BLUE_B).to_corner(UL).shift(DOWN*0.4)
#         self.play(FadeIn(step_title))

#         eq1 = MathTex("P_A(\\lambda)", "=", "|A - \\lambda I_2|", font_size=BODY_MATH_SIZE)
#         eq2 = MathTex("=", "\\begin{vmatrix} 1-\\lambda & 2 \\\\ -1 & 4-\\lambda \\end{vmatrix}", font_size=BODY_MATH_SIZE)
#         eq3 = MathTex("=", "(1-\\lambda)(4-\\lambda) - (-1)(2)", font_size=BODY_MATH_SIZE)
#         eq4 = MathTex("=", "\\lambda^2 - 5\\lambda + 6", font_size=BODY_MATH_SIZE)

#         math_block = VGroup(eq1, eq2, eq3, eq4).arrange(DOWN, buff=0.3)
        
#         for eq in math_block[1:]:
#             eq[0].set_x(eq1[1].get_x())             
#             eq[1].next_to(eq[0], RIGHT, buff=0.2)   

#         math_block.next_to(step_title, DOWN, buff=0.5).shift(RIGHT * 1.5)

#         self.play(Write(eq1))
#         self.wait(0.5)

#         self.play(FadeIn(eq2[0]), TransformFromCopy(eq1[2], eq2[1]), run_time=1.2)
#         self.wait(0.5)

#         self.play(FadeIn(eq3[0]), TransformFromCopy(eq2[1], eq3[1]), run_time=1.2)
#         self.wait(0.5)

#         self.play(FadeIn(eq4[0]), TransformFromCopy(eq3[1], eq4[1]), run_time=1.2)
#         self.wait(1)

#         eq_zero = MathTex("\\Rightarrow \\lambda^2 - 5\\lambda + 6 = 0", font_size=BODY_MATH_SIZE)
#         eq_zero.next_to(math_block, DOWN, buff=0.4).align_to(eq1[0], LEFT)
        
#         self.play(Write(eq_zero))
#         self.wait(1)

#         final_lambdas = MathTex(
#             "\\Leftrightarrow \\left[ \\begin{aligned} \\lambda_1 &= 2 \\\\ \\lambda_2 &= 3 \\end{aligned} \\right.", 
#             font_size=BODY_MATH_SIZE
#         )
#         final_lambdas.next_to(eq_zero, DOWN, buff=0.4).align_to(eq_zero, LEFT)
#         final_lambdas.set_color(C_LAMBDA)
        
#         box = SurroundingRectangle(final_lambdas, color=C_LAMBDA, buff=0.2)
#         self.play(Write(final_lambdas), Create(box))
#         self.wait(2)

#         lambdas_ref = MathTex("\\lambda_1 = 2, \\lambda_2 = 3", font_size=NOTE_MATH_SIZE).set_color(C_LAMBDA).to_corner(UR)
#         self.play(
#             FadeOut(step_title), FadeOut(math_block), FadeOut(eq_zero),
#             ReplacementTransform(VGroup(final_lambdas, box), lambdas_ref)
#         )
#         return lambdas_ref

#     def step2_find_eigenvector(self, step_name, lam_val, mat_before, transform_op, mat_after, eq_str, vec_res, u_subscript, ref_pos_shift, anchor):
#         step_title = Text(step_name, font=VN_FONT, font_size=BODY_TEXT_SIZE, color=BLUE_B).to_corner(UL).shift(DOWN*0.8)
#         lam_text = MathTex("\\lambda = " + lam_val, font_size=BODY_MATH_SIZE).set_color(C_LAMBDA).next_to(step_title, RIGHT)
#         self.play(FadeIn(step_title), Write(lam_text))

#         # 1. DÒNG "ẨN TỰ DO"
#         t_p1 = Text("Đặt", font=VN_FONT, font_size=BODY_TEXT_SIZE)
#         t_p2 = MathTex("x_2 = t", font_size=BODY_MATH_SIZE)
#         t_p3 = Text("là ẩn tự do", font=VN_FONT, font_size=BODY_TEXT_SIZE)
#         t_p4 = MathTex("\\Rightarrow X = t \\begin{pmatrix} " + vec_res + " \\end{pmatrix}", font_size=BODY_MATH_SIZE)
        
#         t_step = VGroup(t_p1, t_p2, t_p3, t_p4).arrange(RIGHT, buff=0.15)

#         # 2. DÒNG "VECTOR RIÊNG TƯƠNG ỨNG LÀ"
#         u_arrow = MathTex("\\Rightarrow", font_size=BODY_MATH_SIZE)
#         u_text = Text("Vector riêng tương ứng là:", font=VN_FONT, font_size=BODY_TEXT_SIZE)
#         u_math = MathTex("u_" + u_subscript + " = \\begin{pmatrix} " + vec_res + " \\end{pmatrix}", font_size=BODY_MATH_SIZE).set_color(C_VECTOR)
        
#         u_step = VGroup(u_arrow, u_text, u_math).arrange(RIGHT, buff=0.15)

#         matrix_transform_str = mat_before + " \\xrightarrow{" + transform_op + "} " + mat_after
        
#         content = VGroup(
#             MathTex("(A - " + lam_val + "I_2)X = 0", font_size=BODY_MATH_SIZE),
#             MathTex(matrix_transform_str, font_size=BODY_MATH_SIZE),
#             MathTex("\\Rightarrow " + eq_str, font_size=BODY_MATH_SIZE),
#             t_step,
#             u_step
#         ).arrange(DOWN, buff=0.4).next_to(step_title, DOWN, buff=0.5).to_edge(LEFT, buff=1.5)

#         self.play(Write(content[0]))
#         self.play(FadeIn(content[1], shift=UP))
#         self.play(Write(content[2]))
#         self.play(FadeIn(content[3], shift=UP))
#         self.play(Write(content[4]))
        
#         self.play(Circumscribe(content[4][2], color=C_VECTOR, time_width=2))
#         self.wait(1.5)

#         u_ref = MathTex("u_" + u_subscript + " = \\begin{pmatrix} " + vec_res + " \\end{pmatrix}", font_size=NOTE_MATH_SIZE).set_color(C_VECTOR).next_to(anchor, DOWN, buff=0.3).shift(ref_pos_shift).align_to(anchor, RIGHT)
        
#         self.play(
#             FadeOut(VGroup(step_title, lam_text, content)),
#             ReplacementTransform(content[4][2].copy(), u_ref) 
#         )
#         return u_ref

#     def step3_build_matrices(self, u1_ref, u2_ref):
#         step_title = Text("Lập ma trận P và thực hiện chéo hóa", font=VN_FONT, font_size=BODY_TEXT_SIZE, color=BLUE_B).to_corner(UL).shift(DOWN*0.5)
#         self.play(FadeIn(step_title))

#         mat_P_label = Text("Lập ma trận P từ các vector riêng:", font=VN_FONT, font_size=NOTE_TEXT_SIZE)
#         mat_P = MathTex("P", "=", "\\begin{pmatrix} 2 & 1 \\\\ 1 & 1 \\end{pmatrix}", font_size=BODY_MATH_SIZE)
#         mat_P[0].set_color(C_VECTOR)

#         group_P = VGroup(mat_P_label, mat_P).arrange(RIGHT, buff=0.4)
#         group_P.next_to(step_title, DOWN, buff=0.3).to_edge(LEFT, buff=1.5)

#         self.play(Write(mat_P_label), Write(mat_P))
        
#         box_u1 = SurroundingRectangle(mat_P[2][0:2], color=GREEN_C, buff=0.1) 
#         box_u2 = SurroundingRectangle(mat_P[2][2:4], color=GREEN_E, buff=0.1) 
        
#         self.play(Create(box_u1), Indicate(u1_ref, color=WHITE))
#         self.play(ReplacementTransform(box_u1, box_u2), Indicate(u2_ref, color=WHITE))
#         self.play(FadeOut(box_u2))
#         self.wait(0.5)

#         calc_label = Text("Thực hiện phép tính:", font=VN_FONT, font_size=NOTE_TEXT_SIZE)
#         calc_label.next_to(group_P, DOWN, buff=0.3).align_to(step_title, LEFT)
#         self.play(Write(calc_label))

#         CALC_FONT_SIZE = 30 

#         eq1 = MathTex("P^{-1}", "A", "P", "=", "\\begin{pmatrix} 2 & 1 \\\\ 1 & 1 \\end{pmatrix}^{-1} \\begin{pmatrix} 1 & 2 \\\\ -1 & 4 \\end{pmatrix} \\begin{pmatrix} 2 & 1 \\\\ 1 & 1 \\end{pmatrix}", font_size=CALC_FONT_SIZE)
#         eq2 = MathTex("=", "\\begin{pmatrix} 1 & -1 \\\\ -1 & 2 \\end{pmatrix} \\begin{pmatrix} 1 & 2 \\\\ -1 & 4 \\end{pmatrix} \\begin{pmatrix} 2 & 1 \\\\ 1 & 1 \\end{pmatrix}", font_size=CALC_FONT_SIZE)
#         eq3 = MathTex("=", "\\begin{pmatrix} 2 & 0 \\\\ 0 & 3 \\end{pmatrix}", font_size=CALC_FONT_SIZE)
        
#         eq1[0].set_color(C_VECTOR)  
#         eq1[1].set_color(C_MAIN)    
#         eq1[2].set_color(C_VECTOR)  
#         eq3[1].set_color(C_LAMBDA)  

#         math_block = VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.25)
#         for eq in math_block[1:]:
#             eq[0].set_x(eq1[3].get_x())             
#             eq[1].next_to(eq[0], RIGHT, buff=0.2)

#         math_block.next_to(calc_label, DOWN, buff=0.25).align_to(calc_label, LEFT).shift(RIGHT * 1.5)

#         self.play(Write(eq1))
#         self.wait(1)
        
#         self.play(FadeIn(eq2[0]), TransformFromCopy(eq1[4], eq2[1]), run_time=1.5)
#         self.wait(1)
        
#         self.play(FadeIn(eq3[0]), TransformFromCopy(eq2[1], eq3[1]), run_time=1.5)
#         self.wait(1)

#         eq4 = MathTex("=", "D", font_size=CALC_FONT_SIZE)
#         eq4[1].set_color(C_LAMBDA)
#         eq4.next_to(eq3[1], RIGHT, buff=0.3)
        
#         self.play(Write(eq4))
        
#         final_group = VGroup(eq1, eq2, eq3, eq4)
#         final_box = SurroundingRectangle(final_group, color=YELLOW, buff=0.2)
        
#         self.play(Create(final_box))
#         self.play(Flash(final_box, color=YELLOW))
#         self.wait(4)























from manim import *
import numpy as np
import math
from PIL import Image
import os

# BẢNG MÀU TỔNG HỢP (Đã được hợp nhất 100% xuyên suốt)
VN_FONT = "Arial"
C_MAIN = BLUE_C      
C_LAMBDA = YELLOW  

# BỘ MÀU MA TRẬN SVD CHUẨN (Áp dụng cho mọi Video)
C_U = "#58C4DD"      # Xanh lơ sáng (Ma trận U)
C_SIGMA = "#83C167"  # Xanh lục (Ma trận Sigma)
C_V = "#FC6255"      # Đỏ nhạt (Ma trận V)

C_VECTOR = C_V       
C_SVD = C_SIGMA      


C_TITLE = WHITE
C_MATH = WHITE
C_VEC_1 = TEAL_C
C_VEC_2 = RED_C
C_GRID = BLUE_E

# KÍCH THƯỚC CHỮ
TITLE_SIZE = 32           
SUBTITLE_SIZE = 26        
FORMULA_MAIN_SIZE = 56    

BODY_TEXT_SIZE = 24       
BODY_MATH_SIZE = 36       

NOTE_TEXT_SIZE = 20      
NOTE_MATH_SIZE = 28      


# Đoạn video số 1
class Section1_IntroProblem(Scene):
    def construct(self):
        title = Text("PHÂN RÃ SVD VÀ CHÉO HÓA", font=VN_FONT, font_size=42, weight=BOLD)
        title.to_edge(UP, buff=1.5)
        
        subtitle = Text("Giới thiệu ma trận nghiên cứu:", font=VN_FONT, font_size=SUBTITLE_SIZE, color=LIGHT_GREY)
        subtitle.next_to(title, DOWN, buff=1)

        matrix_A = MathTex("A", "=", "\\begin{pmatrix} 1 & 2 \\\\ -1 & 4 \\end{pmatrix}", font_size=FORMULA_MAIN_SIZE)
        matrix_A.next_to(subtitle, DOWN, buff=0.5)
        matrix_A[0].set_color(C_MAIN)

        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=DOWN))
        self.play(Write(matrix_A))
        self.play(Indicate(matrix_A[0], color=C_MAIN, scale_factor=1.2))
        self.wait(2)

        self.play(FadeOut(VGroup(title, subtitle, matrix_A)))




# Đoạn video số 2
class MatrixDiagonalization(Scene):
    def construct(self):
        main_title = Text("4. Bài toán chéo hóa ma trận", font=VN_FONT, font_size=TITLE_SIZE, color=C_SVD).to_corner(UL)
        self.play(FadeIn(main_title))

        res_lambdas = self.step1_find_eigenvalues()
        res_u1 = self.step2_find_eigenvector(
            step_name="Tìm vector riêng cho",
            lam_val="2",
            mat_before="\\begin{pmatrix} 1-2 & 2 \\\\ -1 & 4-2 \\end{pmatrix}",
            transform_op="d_2 - d_1", 
            mat_after="\\begin{pmatrix} -1 & 2 \\\\ 0 & 0 \\end{pmatrix}",
            eq_str="-x_1 + 2x_2 = 0",
            vec_res="2 \\\\ 1",
            u_subscript="1", 
            ref_pos_shift=ORIGIN,
            anchor=res_lambdas
        )
        res_u2 = self.step2_find_eigenvector(
            step_name="Tìm vector riêng cho",
            lam_val="3",
            mat_before="\\begin{pmatrix} 1-3 & 2 \\\\ -1 & 4-3 \\end{pmatrix}",
            transform_op="2d_2 - d_1", 
            mat_after="\\begin{pmatrix} -2 & 2 \\\\ 0 & 0 \\end{pmatrix}",
            eq_str="-2x_1 + 2x_2 = 0 \\Rightarrow -x_1 + x_2 = 0",
            vec_res="1 \\\\ 1",
            u_subscript="2", 
            ref_pos_shift=DOWN*1.2,
            anchor=res_lambdas
        )
        self.step3_build_matrices(res_u1, res_u2)

    def step1_find_eigenvalues(self):
        step_title = Text("Tìm đa thức đặc trưng và trị riêng", font=VN_FONT, font_size=BODY_TEXT_SIZE, color=BLUE_B).to_corner(UL).shift(DOWN*0.4)
        self.play(FadeIn(step_title))

        eq1 = MathTex("P_A(\\lambda)", "=", "|A - \\lambda I_2|", font_size=BODY_MATH_SIZE)
        eq2 = MathTex("=", "\\begin{vmatrix} 1-\\lambda & 2 \\\\ -1 & 4-\\lambda \\end{vmatrix}", font_size=BODY_MATH_SIZE)
        eq3 = MathTex("=", "(1-\\lambda)(4-\\lambda) - (-1)(2)", font_size=BODY_MATH_SIZE)
        eq4 = MathTex("=", "\\lambda^2 - 5\\lambda + 6", font_size=BODY_MATH_SIZE)

        math_block = VGroup(eq1, eq2, eq3, eq4).arrange(DOWN, buff=0.3)
        
        for eq in math_block[1:]:
            eq[0].set_x(eq1[1].get_x())             
            eq[1].next_to(eq[0], RIGHT, buff=0.2)   

        math_block.next_to(step_title, DOWN, buff=0.5).shift(RIGHT * 1.5)

        self.play(Write(eq1))
        self.wait(0.5)

        self.play(FadeIn(eq2[0]), TransformFromCopy(eq1[2], eq2[1]), run_time=1.2)
        self.wait(0.5)

        self.play(FadeIn(eq3[0]), TransformFromCopy(eq2[1], eq3[1]), run_time=1.2)
        self.wait(0.5)

        self.play(FadeIn(eq4[0]), TransformFromCopy(eq3[1], eq4[1]), run_time=1.2)
        self.wait(1)

        eq_zero = MathTex("\\Rightarrow \\lambda^2 - 5\\lambda + 6 = 0", font_size=BODY_MATH_SIZE)
        eq_zero.next_to(math_block, DOWN, buff=0.4).align_to(eq1[0], LEFT)
        
        self.play(Write(eq_zero))
        self.wait(1)

        final_lambdas = MathTex(
            "\\Leftrightarrow \\left[ \\begin{aligned} \\lambda_1 &= 2 \\\\ \\lambda_2 &= 3 \\end{aligned} \\right.", 
            font_size=BODY_MATH_SIZE
        )
        final_lambdas.next_to(eq_zero, DOWN, buff=0.4).align_to(eq_zero, LEFT)
        final_lambdas.set_color(C_LAMBDA)
        
        box = SurroundingRectangle(final_lambdas, color=C_LAMBDA, buff=0.2)
        self.play(Write(final_lambdas), Create(box))
        self.wait(2)

        lambdas_ref = MathTex("\\lambda_1 = 2, \\lambda_2 = 3", font_size=NOTE_MATH_SIZE).set_color(C_LAMBDA).to_corner(UR)
        self.play(
            FadeOut(step_title), FadeOut(math_block), FadeOut(eq_zero),
            ReplacementTransform(VGroup(final_lambdas, box), lambdas_ref)
        )
        return lambdas_ref

    def step2_find_eigenvector(self, step_name, lam_val, mat_before, transform_op, mat_after, eq_str, vec_res, u_subscript, ref_pos_shift, anchor):
        step_title = Text(step_name, font=VN_FONT, font_size=BODY_TEXT_SIZE, color=BLUE_B).to_corner(UL).shift(DOWN*0.8)
        lam_text = MathTex("\\lambda = " + lam_val, font_size=BODY_MATH_SIZE).set_color(C_LAMBDA).next_to(step_title, RIGHT)
        self.play(FadeIn(step_title), Write(lam_text))

        # 1. DÒNG "ẨN TỰ DO"
        t_p1 = Text("Đặt", font=VN_FONT, font_size=BODY_TEXT_SIZE)
        t_p2 = MathTex("x_2 = t", font_size=BODY_MATH_SIZE)
        t_p3 = Text("là ẩn tự do", font=VN_FONT, font_size=BODY_TEXT_SIZE)
        t_p4 = MathTex("\\Rightarrow X = t \\begin{pmatrix} " + vec_res + " \\end{pmatrix}", font_size=BODY_MATH_SIZE)
        
        t_step = VGroup(t_p1, t_p2, t_p3, t_p4).arrange(RIGHT, buff=0.15)

        # 2. DÒNG "VECTOR RIÊNG TƯƠNG ỨNG LÀ"
        u_arrow = MathTex("\\Rightarrow", font_size=BODY_MATH_SIZE)
        u_text = Text("Vector riêng tương ứng là:", font=VN_FONT, font_size=BODY_TEXT_SIZE)
        u_math = MathTex("u_" + u_subscript + " = \\begin{pmatrix} " + vec_res + " \\end{pmatrix}", font_size=BODY_MATH_SIZE).set_color(C_VECTOR)
        
        u_step = VGroup(u_arrow, u_text, u_math).arrange(RIGHT, buff=0.15)

        matrix_transform_str = mat_before + " \\xrightarrow{" + transform_op + "} " + mat_after
        
        content = VGroup(
            MathTex("(A - " + lam_val + "I_2)X = 0", font_size=BODY_MATH_SIZE),
            MathTex(matrix_transform_str, font_size=BODY_MATH_SIZE),
            MathTex("\\Rightarrow " + eq_str, font_size=BODY_MATH_SIZE),
            t_step,
            u_step
        ).arrange(DOWN, buff=0.4).next_to(step_title, DOWN, buff=0.5).to_edge(LEFT, buff=1.5)

        self.play(Write(content[0]))
        self.play(FadeIn(content[1], shift=UP))
        self.play(Write(content[2]))
        self.play(FadeIn(content[3], shift=UP))
        self.play(Write(content[4]))
        
        self.play(Circumscribe(content[4][2], color=C_VECTOR, time_width=2))
        self.wait(1.5)

        u_ref = MathTex("u_" + u_subscript + " = \\begin{pmatrix} " + vec_res + " \\end{pmatrix}", font_size=NOTE_MATH_SIZE).set_color(C_VECTOR).next_to(anchor, DOWN, buff=0.3).shift(ref_pos_shift).align_to(anchor, RIGHT)
        
        self.play(
            FadeOut(VGroup(step_title, lam_text, content)),
            ReplacementTransform(content[4][2].copy(), u_ref) 
        )
        return u_ref

    def step3_build_matrices(self, u1_ref, u2_ref):
        step_title = Text("Lập ma trận P và thực hiện chéo hóa", font=VN_FONT, font_size=BODY_TEXT_SIZE, color=BLUE_B).to_corner(UL).shift(DOWN*0.5)
        self.play(FadeIn(step_title))

        mat_P_label = Text("Lập ma trận P từ các vector riêng:", font=VN_FONT, font_size=NOTE_TEXT_SIZE)
        mat_P = MathTex("P", "=", "\\begin{pmatrix} 2 & 1 \\\\ 1 & 1 \\end{pmatrix}", font_size=BODY_MATH_SIZE)
        mat_P[0].set_color(C_VECTOR)

        group_P = VGroup(mat_P_label, mat_P).arrange(RIGHT, buff=0.4)
        group_P.next_to(step_title, DOWN, buff=0.3).to_edge(LEFT, buff=1.5)

        self.play(Write(mat_P_label), Write(mat_P))
        
        box_u1 = SurroundingRectangle(mat_P[2][0:2], color=GREEN_C, buff=0.1) 
        box_u2 = SurroundingRectangle(mat_P[2][2:4], color=GREEN_E, buff=0.1) 
        
        self.play(Create(box_u1), Indicate(u1_ref, color=WHITE))
        self.play(ReplacementTransform(box_u1, box_u2), Indicate(u2_ref, color=WHITE))
        self.play(FadeOut(box_u2))
        self.wait(0.5)

        calc_label = Text("Thực hiện phép tính:", font=VN_FONT, font_size=NOTE_TEXT_SIZE)
        calc_label.next_to(group_P, DOWN, buff=0.3).align_to(step_title, LEFT)
        self.play(Write(calc_label))

        CALC_FONT_SIZE = 30 

        eq1 = MathTex("P^{-1}", "A", "P", "=", "\\begin{pmatrix} 2 & 1 \\\\ 1 & 1 \\end{pmatrix}^{-1} \\begin{pmatrix} 1 & 2 \\\\ -1 & 4 \\end{pmatrix} \\begin{pmatrix} 2 & 1 \\\\ 1 & 1 \\end{pmatrix}", font_size=CALC_FONT_SIZE)
        eq2 = MathTex("=", "\\begin{pmatrix} 1 & -1 \\\\ -1 & 2 \\end{pmatrix} \\begin{pmatrix} 1 & 2 \\\\ -1 & 4 \\end{pmatrix} \\begin{pmatrix} 2 & 1 \\\\ 1 & 1 \\end{pmatrix}", font_size=CALC_FONT_SIZE)
        eq3 = MathTex("=", "\\begin{pmatrix} 2 & 0 \\\\ 0 & 3 \\end{pmatrix}", font_size=CALC_FONT_SIZE)
        
        eq1[0].set_color(C_VECTOR)  
        eq1[1].set_color(C_MAIN)    
        eq1[2].set_color(C_VECTOR)  
        eq3[1].set_color(C_LAMBDA)  

        math_block = VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.25)
        for eq in math_block[1:]:
            eq[0].set_x(eq1[3].get_x())             
            eq[1].next_to(eq[0], RIGHT, buff=0.2)

        math_block.next_to(calc_label, DOWN, buff=0.25).align_to(calc_label, LEFT).shift(RIGHT * 1.5)

        self.play(Write(eq1))
        self.wait(1)
        
        self.play(FadeIn(eq2[0]), TransformFromCopy(eq1[4], eq2[1]), run_time=1.5)
        self.wait(1)
        
        self.play(FadeIn(eq3[0]), TransformFromCopy(eq2[1], eq3[1]), run_time=1.5)
        self.wait(1)

        eq4 = MathTex("=", "D", font_size=CALC_FONT_SIZE)
        eq4[1].set_color(C_LAMBDA)
        eq4.next_to(eq3[1], RIGHT, buff=0.3)
        
        self.play(Write(eq4))
        
        final_group = VGroup(eq1, eq2, eq3, eq4)
        final_box = SurroundingRectangle(final_group, color=YELLOW, buff=0.2)
        
        self.play(Create(final_box))
        self.play(Flash(final_box, color=YELLOW))
        self.wait(4)


# Bảng map màu tự động cho phương trình chứng minh
MAP = {
    "U": C_U, "V": C_V, "P": C_V,
    "U^T": C_U, "V^T": C_V, "P^T": C_V, "P^{-1}": C_V,
    "\\Sigma": C_SIGMA, "\\Sigma^T": C_SIGMA, "\\Lambda": C_LAMBDA,
    "A": C_MAIN, "A^T": C_MAIN, "I": WHITE
}
# Đoạn video số 3
class SVDAndDiagonalization(Scene):
    def construct(self):
        main_title = Text("5. Mối liên hệ bản chất giữa SVD và Chéo hóa", font=VN_FONT, font_size=TITLE_SIZE, color=C_SVD).to_corner(UL)
        self.play(FadeIn(main_title))

        # ==========================================
        # BƯỚC 1: KHAI TRIỂN SVD CỦA A^T A
        # ==========================================
        step1_title = Text("1. Khai triển SVD của ma trận đối xứng", font=VN_FONT, font_size=BODY_TEXT_SIZE, color=BLUE_B)
        step1_title.next_to(main_title, DOWN, buff=0.3).to_edge(LEFT, buff=1.5)
        self.play(FadeIn(step1_title))

        eq1 = MathTex("A", "=", "U \\Sigma V^T", tex_to_color_map=MAP, font_size=BODY_MATH_SIZE)
        eq2 = MathTex("A^T", "=", "(U \\Sigma V^T)^T", "=", "V \\Sigma^T U^T", tex_to_color_map=MAP, font_size=BODY_MATH_SIZE)
        eq3 = MathTex("A^T A", "=", "(V \\Sigma^T U^T)", "(U \\Sigma V^T)", tex_to_color_map=MAP, font_size=BODY_MATH_SIZE)
        eq4 = MathTex("=", "V \\Sigma^T", "(U^T U)", "\\Sigma V^T", tex_to_color_map=MAP, font_size=BODY_MATH_SIZE)
        eq5 = MathTex("=", "V \\Sigma^T", "I", "\\Sigma V^T", tex_to_color_map=MAP, font_size=BODY_MATH_SIZE)
        eq6 = MathTex("A^T A", "=", "V", "(\\Sigma^T \\Sigma)", "V^T", tex_to_color_map=MAP, font_size=BODY_MATH_SIZE)

        math_block_1 = VGroup(eq1, eq2, eq3, eq4, eq5, eq6).arrange(DOWN, buff=0.15)
        math_block_1.next_to(step1_title, DOWN, buff=0.2).shift(RIGHT * 1)

        eq_indices = [1, 1, 1, 0, 0, 1] 
        target_x = eq3[1].get_center()[0]
        for eq, idx in zip(math_block_1, eq_indices):
            eq.shift(RIGHT * (target_x - eq[idx].get_center()[0]))

        self.play(Write(eq1))
        self.play(FadeIn(eq2[0:2]), TransformFromCopy(eq1[2], eq2[2]), run_time=0.8)
        self.play(Write(eq2[3:]))
        self.play(FadeIn(eq3[0:2]), TransformFromCopy(eq2[4], eq3[2]), TransformFromCopy(eq1[2], eq3[3]), run_time=1)
        self.play(FadeIn(eq4[0]), TransformFromCopy(eq3[2:], eq4[1:]), run_time=1)
        
        # brace_U = Brace(eq4[2], DOWN, color=C_VECTOR)
        # text_brace_vn = Text("Ma trận trực giao", font=VN_FONT, font_size=NOTE_TEXT_SIZE-2, color=C_VECTOR)
        # math_brace_i = MathTex("(= I)", font_size=NOTE_MATH_SIZE-2, color=C_VECTOR)
        brace_U = Brace(eq4[2], DOWN, color=C_U)
        text_brace_vn = Text("Ma trận trực giao", font=VN_FONT, font_size=NOTE_TEXT_SIZE-2, color=C_U)
        math_brace_i = MathTex("(= I)", font_size=NOTE_MATH_SIZE-2, color=C_U)
        text_U = VGroup(text_brace_vn, math_brace_i).arrange(RIGHT, buff=0.1).next_to(brace_U, DOWN, buff=0.05)
        
        self.play(GrowFromCenter(brace_U), FadeIn(text_U, shift=UP))
        self.wait(1)

        self.play(
            FadeIn(eq5[0]),
            TransformFromCopy(eq4[1], eq5[1]),
            TransformFromCopy(eq4[2], eq5[2]), 
            TransformFromCopy(eq4[3], eq5[3]),
            FadeOut(brace_U), FadeOut(text_U),
            run_time=1
        )
        self.wait(0.5)
        
        self.play(FadeIn(eq6[0:2]), TransformFromCopy(eq5[1:], eq6[2:]), run_time=1)
        self.wait(1)

        self.play(
            FadeOut(eq1), FadeOut(eq2), FadeOut(eq3), FadeOut(eq4), FadeOut(eq5),
            eq6.animate.next_to(step1_title, DOWN, buff=0.3).align_to(eq6, LEFT)
        )

        # ==========================================
        # BƯỚC 2: SO SÁNH VỚI CHÉO HÓA (Đã sửa lỗi text dài)
        # ==========================================
        step2_title = Text("2. So sánh với Chéo hóa ma trận đối xứng", font=VN_FONT, font_size=BODY_TEXT_SIZE, color=BLUE_B)
        step2_title.next_to(eq6, DOWN, buff=0.4).to_edge(LEFT, buff=1.5)
        self.play(FadeIn(step2_title))

        eq_d1 = MathTex("A^T A", "=", "P", "\\Lambda", "P^{-1}", tex_to_color_map=MAP, font_size=BODY_MATH_SIZE)
        eq_d1.next_to(step2_title, DOWN, buff=0.25)
        eq_d1.shift(RIGHT * (target_x - eq_d1[1].get_center()[0]))
        
        # Tạo dòng chú thích ngắn gọn, chia thành các cụm VGroup để giữ màu sắc
        note_1 = Text("Vì ", font=VN_FONT, font_size=NOTE_TEXT_SIZE, color=GRAY)
        note_m1 = MathTex("A^T A", font_size=NOTE_MATH_SIZE, color=C_MAIN)
        note_2 = Text(" đối xứng, nó chéo hóa trực giao được (", font=VN_FONT, font_size=NOTE_TEXT_SIZE, color=GRAY)
        note_m2 = MathTex("P^{-1} = P^T", font_size=NOTE_MATH_SIZE, color=C_VECTOR)
        note_3 = Text("):", font=VN_FONT, font_size=NOTE_TEXT_SIZE, color=GRAY)
        note_group = VGroup(note_1, note_m1, note_2, note_m2, note_3).arrange(RIGHT, buff=0.1)
        note_group.next_to(eq_d1, DOWN, buff=0.15).align_to(eq_d1, LEFT).shift(LEFT * 0.5)

        eq_d2 = MathTex("A^T A", "=", "P", "\\Lambda", "P^T", tex_to_color_map=MAP, font_size=BODY_MATH_SIZE)
        eq_d2.next_to(note_group, DOWN, buff=0.15)
        eq_d2.shift(RIGHT * (target_x - eq_d2[1].get_center()[0]))

        self.play(Write(eq_d1))
        self.play(FadeIn(note_group, shift=LEFT))
        self.play(FadeIn(eq_d2[0:2]), TransformFromCopy(eq_d1[2:], eq_d2[2:]), run_time=1.2)
        self.wait(1.5)

        # ==========================================
        # BƯỚC 3: ĐỒNG NHẤT HÓA (THE AHA! MOMENT)
        # ==========================================
        comp_eq = MathTex("V", "(\\Sigma^T \\Sigma)", "V^T", "=", "P", "\\Lambda", "P^T", tex_to_color_map=MAP, font_size=BODY_MATH_SIZE + 5)
        comp_eq.move_to(UP * 0.5)

        self.play(
            FadeOut(step1_title), FadeOut(step2_title), FadeOut(note_group),
            ReplacementTransform(eq6[2], comp_eq[0]),
            ReplacementTransform(eq6[3], comp_eq[1]),
            ReplacementTransform(eq6[4], comp_eq[2]),
            ReplacementTransform(eq_d2[2], comp_eq[4]),
            ReplacementTransform(eq_d2[3], comp_eq[5]),
            ReplacementTransform(eq_d2[4], comp_eq[6]),
            FadeOut(eq6[0:2]), FadeOut(eq_d1), FadeOut(eq_d2[0:2]), 
            FadeIn(comp_eq[3]), 
            run_time=1.5
        )
        
        exp_text = Text("Cả hai đều là ma trận vector riêng của phân tích chéo hóa", font=VN_FONT, font_size=NOTE_TEXT_SIZE, color=GRAY)
        exp_math = MathTex("\\Rightarrow V = P", font_size=BODY_MATH_SIZE)
        exp_math[0][1].set_color(C_VECTOR)
        exp_math[0][3].set_color(C_VECTOR)
        exp_group = VGroup(exp_text, exp_math).arrange(DOWN, buff=0.2).next_to(comp_eq, DOWN, buff=0.5)
        
        self.play(FadeIn(exp_group, shift=UP))
        self.wait(1.5)

        core_eq = MathTex("\\Sigma^T \\Sigma", "=", "\\Lambda", tex_to_color_map=MAP, font_size=BODY_MATH_SIZE + 10)
        core_eq.next_to(exp_group, DOWN, buff=0.5)

        # SỬA LỖI: Dùng TransformFromCopy để không làm mất V và P ở phương trình comp_eq
        self.play(
            TransformFromCopy(comp_eq[1], core_eq[0]),
            TransformFromCopy(comp_eq[3], core_eq[1]),
            TransformFromCopy(comp_eq[5], core_eq[2]),
            run_time=1.5
        )
        self.play(core_eq[2].animate.set_color(C_SVD)) # Aha moment
        self.wait(1)

        # ==========================================
        # BƯỚC 4: KẾT LUẬN TOÁN HỌC MƯỢT MÀ 
        # ==========================================
        # Đẩy phương trình lõi lên trên một cách mềm mại (Lúc này mới xóa comp_eq và chữ giải thích đi)
        self.play(
            FadeOut(comp_eq), FadeOut(exp_group),
            core_eq.animate.move_to(UP * 1.5).scale(1.2),
            run_time=1.5
        )
        self.wait(0.5)

        diag_text = Text("Xét các phần tử trên đường chéo chính, ta có:", font=VN_FONT, font_size=BODY_TEXT_SIZE, color=BLUE_A)
        diag_text.next_to(core_eq, DOWN, buff=0.6)
        self.play(Write(diag_text))

        res2 = MathTex("\\sigma_i^2", "=", "\\lambda_i", tex_to_color_map={"\\sigma_i^2": C_SVD, "\\lambda_i": C_SVD}, font_size=BODY_MATH_SIZE + 10)
        res2.next_to(diag_text, DOWN, buff=0.4)

        self.play(
            TransformFromCopy(core_eq[0], res2[0]), 
            TransformFromCopy(core_eq[1], res2[1]), 
            TransformFromCopy(core_eq[2], res2[2]), 
            run_time=1.5
        )
        self.wait(1)

        res3_arrow = MathTex("\\Rightarrow", font_size=BODY_MATH_SIZE + 10)
        res3_math = MathTex(
            r"\sigma_i = \sqrt{\lambda_i(A^T A)}",
            tex_to_color_map={r"\sigma_i": C_SVD, r"\lambda_i": C_SVD, "A": C_MAIN},
            font_size=BODY_MATH_SIZE + 20 
        )
        res3_group = VGroup(res3_arrow, res3_math).arrange(RIGHT, buff=0.4)
        res3_group.next_to(res2, DOWN, buff=0.6)

        self.play(
            FadeIn(res3_arrow, shift=RIGHT), 
            ReplacementTransform(res2.copy(), res3_math), 
            run_time=1.5
        )
        
        final_box = SurroundingRectangle(res3_math, color=YELLOW, buff=0.3)
        self.play(Create(final_box, run_time=1.5))
        self.play(Flash(final_box, color=YELLOW, line_length=0.4))
        
        mobs_to_dim = [diag_text, res2, res3_arrow, core_eq]
        self.play(*[m.animate.set_opacity(0.2) for m in mobs_to_dim])
        self.wait(3)







# Đoạn video số 4
class Section23_Theory_And_GeometricSVD(Scene):
    def construct(self):
        # Đổi màu nền Premium (sẽ áp dụng cho cả scene lý thuyết và hình học)
        self.camera.background_color = "#0d1117"
        
        self.show_theory()
        self.show_geometry()

    def show_theory(self):
        # KHÔNG THAY ĐỔI: Phần lý thuyết đã được tối ưu typography từ trước
        title = Text("2. Cơ sở lý thuyết phân rã SVD", font=VN_FONT, font_size=TITLE_SIZE, color=C_SVD).to_corner(UL)
        self.play(FadeIn(title))

        intro_text = Text("Dạng phân rã tổng quát cho ma trận bất kỳ:", font=VN_FONT, font_size=SUBTITLE_SIZE).shift(UP*2.2)
        formula = MathTex("A", "=", "U", "\\Sigma", "V^T", font_size=FORMULA_MAIN_SIZE).next_to(intro_text, DOWN, buff=0.4)
        formula[0].set_color(C_MAIN)
        formula[2].set_color(C_U)
        formula[3].set_color(C_SIGMA)
        formula[4].set_color(C_V)

        self.play(Write(intro_text), FadeIn(formula, shift=UP))
        self.wait(1)

        u_line = VGroup(
            MathTex("U \\in \\mathbb{R}^{m \\times m}", font_size=BODY_MATH_SIZE, color=C_U),
            Text(": Ma trận trực giao", font=VN_FONT, font_size=BODY_TEXT_SIZE),
            MathTex("(U^T U = I)", font_size=BODY_MATH_SIZE)
        ).arrange(RIGHT, buff=0.2)
        u_sub = Text("Các cột là vector suy biến trái (left singular vectors)", font=VN_FONT, font_size=NOTE_TEXT_SIZE, color=LIGHT_GREY)
        u_block = VGroup(u_line, u_sub).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        sigma_line = VGroup(
            MathTex("\\Sigma \\in \\mathbb{R}^{m \\times n}", font_size=BODY_MATH_SIZE, color=C_SIGMA),
            Text(": Ma trận đường chéo", font=VN_FONT, font_size=BODY_TEXT_SIZE),
            MathTex("\\Sigma = \\text{diag}(\\sigma_1, \\dots, \\sigma_p)", font_size=BODY_MATH_SIZE)
        ).arrange(RIGHT, buff=0.2)
        
        sigma_sub = VGroup(
            Text("Với", font=VN_FONT, font_size=NOTE_TEXT_SIZE, color=LIGHT_GREY),
            MathTex("p = \\min(m, n)", font_size=NOTE_MATH_SIZE, color=LIGHT_GREY),
            Text("và", font=VN_FONT, font_size=NOTE_TEXT_SIZE, color=LIGHT_GREY),
            MathTex("\\sigma_1 \\ge \\sigma_2 \\ge \\dots \\ge \\sigma_p \\ge 0", font_size=NOTE_MATH_SIZE, color=LIGHT_GREY)
        ).arrange(RIGHT, buff=0.15)
        sigma_block = VGroup(sigma_line, sigma_sub).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        v_line = VGroup(
            MathTex("V \\in \\mathbb{R}^{n \\times n}", font_size=BODY_MATH_SIZE, color=C_V),
            Text(": Ma trận trực giao", font=VN_FONT, font_size=BODY_TEXT_SIZE),
            MathTex("(V^T V = I)", font_size=BODY_MATH_SIZE)
        ).arrange(RIGHT, buff=0.2)
        v_sub = Text("Các cột là vector suy biến phải (right singular vectors)", font=VN_FONT, font_size=NOTE_TEXT_SIZE, color=LIGHT_GREY)
        v_block = VGroup(v_line, v_sub).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        all_blocks = VGroup(u_block, sigma_block, v_block).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        all_blocks.next_to(formula, DOWN, buff=0.8).to_edge(LEFT, buff=1.5)

        self.play(FadeIn(u_block, shift=RIGHT))
        self.play(FadeIn(sigma_block, shift=RIGHT))
        self.play(FadeIn(v_block, shift=RIGHT))
        self.wait(3)

        self.play(FadeOut(VGroup(title, intro_text, formula, all_blocks)))

    def show_geometry(self):
        # =========================================================
        # [LAYOUT ENGINE] - ĐỊNH NGHĨA CÁC TỌA ĐỘ NEO (ANCHORS)
        # =========================================================
        # 1. Tọa độ Y (Các tầng dọc)
        Y_HEADER = 3.2      # Tầng 1: Tiêu đề 
        Y_LABEL  = 1.8      # Tầng 2a: Tên ma trận
        Y_MATRIX = 0.4      # Tầng 2b: Ma trận số 
        Y_GRID   = -2.2     # Tầng 3: Lưới tọa độ & Trực quan hóa

        # 2. Tọa độ X (Các cột ngang / Panels)
        X_LEFT   = -4.6     # Panel 1 (Đầu vào V)
        X_MID    = 0.0      # Panel 2 (Biến đổi Sigma)
        X_RIGHT  = 4.6      # Panel 3 (Đầu ra U)

        # =========================================================
        # TẦNG 1: HEADER (TIÊU ĐỀ & CÔNG THỨC SVD)
        # =========================================================
        title = Text("3. Ý nghĩa hình học của SVD", font=VN_FONT, font_size=TITLE_SIZE, color=C_SVD).to_corner(UL)
        #self.play(FadeIn(title))

        
        svd_eq = MathTex("A", "=", "U", "\\Sigma", "V^T", font_size=56)
        svd_eq.set_color_by_tex("U", C_U)
        svd_eq.set_color_by_tex("\\Sigma", C_SIGMA)
        svd_eq.set_color_by_tex("V^T", C_V)
        
        # [MINIMAL FIX]: Chỉ dịch công thức xuống Y = 2.6 (nằm an toàn giữa tiêu đề và các ma trận)
        svd_eq.move_to([X_MID, 2.6, 0]) 
        
        self.play(FadeIn(title, shift=DOWN*0.3), Write(svd_eq))

        # =========================================================
        # TRACKERS (THAM SỐ CHUYỂN ĐỘNG HÌNH HỌC)
        # =========================================================
        vt_theta_v = ValueTracker(0)       
        vt_sigma_x = ValueTracker(1.0)     
        vt_sigma_y = ValueTracker(1.0)
        vt_theta_u = ValueTracker(0)       

        def get_V():
            t = vt_theta_v.get_value()
            return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])

        def get_Sigma():
            return np.array([[vt_sigma_x.get_value(), 0], [0, vt_sigma_y.get_value()]])

        def get_U():
            t = vt_theta_u.get_value()
            return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])

        # =========================================================
        # TẦNG 3: VISUALIZATION ROW (LƯỚI TỌA ĐỘ VÀ MŨI TÊN CHỈ DÒNG)
        # =========================================================
        plane_kwargs = {
            "x_range": [-4, 4], "y_range": [-4, 4],
            "x_length": 3.2, "y_length": 3.2, 
            "background_line_style": {"stroke_color": C_GRID, "stroke_width": 1, "stroke_opacity": 0.5},
            "axis_config": {"stroke_color": GREY, "stroke_width": 2}
        }
        
        plane_in  = NumberPlane(**plane_kwargs).move_to([X_LEFT, Y_GRID, 0])
        plane_mid = NumberPlane(**plane_kwargs).move_to([X_MID, Y_GRID, 0])
        plane_out = NumberPlane(**plane_kwargs).move_to([X_RIGHT, Y_GRID, 0])

        self.play(
            LaggedStart(Create(plane_in), Create(plane_mid), Create(plane_out), lag_ratio=0.3), 
            run_time=2
        )

        arrow_1 = MathTex("\\Rightarrow", font_size=40).move_to([(X_LEFT + X_MID)/2, Y_GRID, 0])
        arrow_2 = MathTex("\\Rightarrow", font_size=40).move_to([(X_MID + X_RIGHT)/2, Y_GRID, 0])
        self.play(FadeIn(arrow_1), FadeIn(arrow_2))

        # =========================================================
        # TẦNG 2: MATRIX ROW (NHÃN & MA TRẬN)
        # =========================================================
        lbl_v   = MathTex("V^T", font_size=40, color=C_V).move_to([X_LEFT, Y_LABEL, 0])
        lbl_sig = MathTex("\\Sigma", font_size=40, color=C_SIGMA).move_to([X_MID, Y_LABEL, 0])
        lbl_u   = MathTex("U", font_size=40, color=C_U).move_to([X_RIGHT, Y_LABEL, 0])

        matrix_kwargs = {
            "element_to_mobject_config": {"num_decimal_places": 2, "font_size": 26},
            "h_buff": 1.1, "v_buff": 0.6
        }

        mat_v_dec = always_redraw(lambda: DecimalMatrix(get_V(), **matrix_kwargs).set_color(C_V).move_to([X_LEFT, Y_MATRIX, 0]))
        mat_sig_dec = always_redraw(lambda: DecimalMatrix(get_Sigma(), **matrix_kwargs).set_color(C_SIGMA).move_to([X_MID, Y_MATRIX, 0]))
        mat_u_dec = always_redraw(lambda: DecimalMatrix(get_U(), **matrix_kwargs).set_color(C_U).move_to([X_RIGHT, Y_MATRIX, 0]))

        self.play(
            Write(lbl_v), Write(lbl_sig), Write(lbl_u),
            Write(mat_v_dec), Write(mat_sig_dec), Write(mat_u_dec)
        )

        # =========================================================
        # TẠO HÌNH HỌC (SHAPES VÀ VECTORS) TRONG TẦNG 3
        # =========================================================
        def get_dynamic_shape(mat_func, plane, color_fill):
            def creator():
                mat = mat_func()
                v1_end = mat @ np.array([1, 0])
                v2_end = mat @ np.array([0, 1])

                shape = Circle(radius=1.0).set_stroke(color_fill, 2).set_fill(color_fill, 0.25)
                mat_3x3 = np.eye(3); mat_3x3[:2, :2] = mat
                shape.apply_matrix(mat_3x3)
                shape.move_to(plane.get_origin()) 

                v1 = Arrow(plane.get_origin(), plane.c2p(v1_end[0], v1_end[1]), buff=0, color=C_VEC_1, stroke_width=4, max_tip_length_to_length_ratio=0.15)
                v2 = Arrow(plane.get_origin(), plane.c2p(v2_end[0], v2_end[1]), buff=0, color=C_VEC_2, stroke_width=4, max_tip_length_to_length_ratio=0.15)
                
                return VGroup(shape, v1, v2)
            return always_redraw(creator)

        shape_in  = get_dynamic_shape(get_V, plane_in, C_V)
        shape_mid = get_dynamic_shape(lambda: get_Sigma(), plane_mid, C_SIGMA)
        shape_out = get_dynamic_shape(lambda: get_U() @ get_Sigma(), plane_out, C_U)

        self.play(FadeIn(shape_in), FadeIn(shape_mid), FadeIn(shape_out))
        self.wait(1)

        # =========================================================
        # PIPELINE ANIMATION (BIẾN ĐỔI SVD)
        # =========================================================
        def highlight_matrix(matrix_mob, color):
            return SurroundingRectangle(matrix_mob, color=color, corner_radius=0.1, buff=0.1)

        # --- Nhịp 1: Quay V^T ---
        box_v = highlight_matrix(mat_v_dec, C_V)
        self.play(Create(box_v))
        self.play(vt_theta_v.animate.set_value(PI / 4), run_time=2.5, rate_func=smooth)
        self.play(FadeOut(box_v))
        self.wait(0.5)

        # --- Nhịp 2: Co giãn Sigma ---
        box_sig = highlight_matrix(mat_sig_dec, C_SIGMA)
        self.play(Create(box_sig))
        self.play(
            vt_sigma_x.animate.set_value(1.8),
            vt_sigma_y.animate.set_value(0.6),
            run_time=3, rate_func=smooth
        )
        self.play(FadeOut(box_sig))
        self.wait(0.5)

        # --- Nhịp 3: Quay U ---
        box_u = highlight_matrix(mat_u_dec, C_U)
        self.play(Create(box_u))
        self.play(vt_theta_u.animate.set_value(PI / 6), run_time=2.5, rate_func=smooth)
        self.play(FadeOut(box_u))
        self.wait(1)

        # --- Nhịp 4: Biến đổi tổng hợp ---
        self.play(
            vt_theta_v.animate.set_value(-PI / 3),
            vt_sigma_x.animate.set_value(1.2),
            vt_sigma_y.animate.set_value(1.8),
            vt_theta_u.animate.set_value(-PI / 4),
            run_time=4, rate_func=there_and_back 
        )
        self.wait(2)





#Đoạn video số 5
# Định nghĩa bảng màu chuẩn
# COLOR_U = "#58C4DD"  # Xanh lơ sáng
# COLOR_S = "#83C167"  # Xanh lục
# COLOR_V = "#FC6255"  # Đỏ nhạt

class SVDDecompositionVisual(Scene):
    def construct(self):
        # --- 1. TIÊU ĐỀ VÀ ĐƯỜNG KẺ ---
        title = MathTex("A", "=", "U", "\\Sigma", "V^\\top", font_size=55)
        title[2].set_color(C_U)
        title[3].set_color(C_SIGMA)
        title[4].set_color(C_V)
        
        line = Line(LEFT * 6, RIGHT * 6, color=WHITE, stroke_width=2)
        VGroup(title, line).arrange(DOWN, buff=0.3).to_edge(UP)
        
        self.play(Write(title), Create(line))
        self.wait(0.5)

        # --- 2. MA TRẬN ĐẦY ĐỦ (Thu nhỏ scale để không bị tràn viền) ---
        mat_U_exp = Matrix([
            ["u_{11}", "u_{12}", "\\dots", "u_{1n}"],
            ["u_{21}", "u_{22}", "\\dots", "u_{2n}"],
            ["\\vdots", "\\vdots", "\\ddots", "\\vdots"],
            ["u_{n1}", "u_{n2}", "\\dots", "u_{nn}"]
        ]).set_color(C_U)
        
        mat_S = Matrix([
            ["\\sigma_1", "", "", ""],
            ["", "\\sigma_2", "", ""],
            ["", "", "\\ddots", ""],
            ["", "", "", "\\sigma_n"]
        ]).set_color(C_SIGMA)
        
        mat_V_exp = Matrix([
            ["v_{11}", "v_{21}", "\\dots", "v_{n1}"],
            ["v_{12}", "v_{22}", "\\dots", "v_{n2}"],
            ["\\vdots", "\\vdots", "\\ddots", "\\vdots"],
            ["v_{1n}", "v_{2n}", "\\dots", "v_{nn}"]
        ]).set_color(C_V)

        # Scale 0.75 để đảm bảo an toàn không bao giờ chạm viền hai bên
        matrices = VGroup(mat_U_exp, mat_S, mat_V_exp).arrange(RIGHT, buff=0.4).scale(0.75).shift(UP * 0.5)
        self.play(FadeIn(matrices))
        self.wait(1)

        # --- 3. ÉP THÀNH VECTOR (NGOẶC ĐỨNG YÊN) ---
        vec_u_list = VGroup()
        u_texs = ["\\vec{u}_1", "\\vec{u}_2", "\\dots", "\\vec{u}_n"]
        for i in range(4):
            vec = MathTex(u_texs[i], font_size=42).set_color(C_U)
            vec.move_to(mat_U_exp.get_columns()[i].get_center())
            vec_u_list.add(vec)
            
        vec_v_list = VGroup()
        v_texs = ["\\vec{v}_1^\\top", "\\vec{v}_2^\\top", "\\vdots", "\\vec{v}_n^\\top"]
        for i in range(4):
            vec = MathTex(v_texs[i], font_size=42).set_color(C_V)
            vec.move_to(mat_V_exp.get_rows()[i].get_center())
            vec_v_list.add(vec)

        # Căn giữa dấu chấm lửng cho V
        vec_v_list[2].match_x(vec_v_list[0])

        transform_anims = []
        for i in range(4):
            transform_anims.append(ReplacementTransform(mat_U_exp.get_columns()[i], vec_u_list[i]))
            transform_anims.append(ReplacementTransform(mat_V_exp.get_rows()[i], vec_v_list[i]))
        
        self.play(*transform_anims, run_time=1.5)
        self.wait(1)

        # --- 4. TẠO PHƯƠNG TRÌNH ĐÁY ---
        eq_bottom = MathTex(
            "U", "\\Sigma", "V^\\top", "=",                   # 0, 1, 2, 3
            "\\sigma_1", "\\vec{u}_1", "\\vec{v}_1^\\top",    # 4, 5, 6
            "+",                                              # 7
            "\\sigma_2", "\\vec{u}_2", "\\vec{v}_2^\\top",    # 8, 9, 10
            "+",                                              # 11
            "\\dots",                                         # 12
            "+",                                              # 13
            "\\sigma_n", "\\vec{u}_n", "\\vec{v}_n^\\top",    # 14, 15, 16
            font_size=56  # Kích thước an toàn để nằm trọn vẹn 1 dòng
        ).to_edge(DOWN, buff=0.8)

        # Tô màu vế trái
        eq_bottom[0].set_color(C_U)
        eq_bottom[1].set_color(C_SIGMA)
        eq_bottom[2].set_color(C_V)

        # Tô màu vế phải
        for i in [4, 8, 14]: eq_bottom[i].set_color(C_SIGMA)
        for i in [5, 9, 15]: eq_bottom[i].set_color(C_U)
        for i in [6, 10, 16]: eq_bottom[i].set_color(C_V)

        # Khởi tạo tàng hình toàn bộ vế phải
        for i in range(4, 17): eq_bottom[i].set_opacity(0)

        # In chữ vế trái
        self.play(Write(eq_bottom[0:4]))
        self.wait(0.5)

        # --- 5. ĐỊNH NGHĨA KHUNG VÀNG ---
        u_height = mat_U_exp.get_brackets().height - 0.2
        v_width = mat_V_exp.get_brackets()[1].get_x() - mat_V_exp.get_brackets()[0].get_x() - 0.2

        def get_u_box(idx):
            return Rectangle(width=vec_u_list[idx].width + 0.3, height=u_height, color=YELLOW).move_to(vec_u_list[idx])

        def get_s_box(idx):
            return SurroundingRectangle(mat_S.get_entries()[idx], color=YELLOW, buff=0.15)

        def get_v_box(idx):
            return Rectangle(width=v_width, height=vec_v_list[idx].height + 0.3, color=YELLOW).move_to(vec_v_list[idx])

        rect_u = get_u_box(0)
        rect_s = get_s_box(0)
        rect_v = get_v_box(0)
        
        self.play(Create(rect_u), Create(rect_s), Create(rect_v))

        # --- 6. HÀM THỰC THI GỘP & ĐEM XUỐNG (FIX LỖI MẤT TÍCH) ---
        def execute_step(idx_vector, idx_sigma, target_indices, is_dots=False):
            u_mob = vec_u_list[idx_vector]
            s_mob = mat_S.get_entries()[idx_sigma]
            v_mob = vec_v_list[idx_vector]
            
            if is_dots:
                g_dots1 = MathTex("\\dots", font_size=45).move_to(DOWN * 0.8)
                g_dots2 = MathTex("\\dots", font_size=45).move_to(DOWN * 0.8)
                g_dots3 = MathTex("\\dots", font_size=45).move_to(DOWN * 0.8)
                
                self.play(
                    TransformFromCopy(s_mob, g_dots1),
                    TransformFromCopy(u_mob, g_dots2),
                    TransformFromCopy(v_mob, g_dots3),
                    run_time=1.2
                )
                self.wait(0.3)
                
                target_group = eq_bottom[target_indices[0]]
                target_copy = target_group.copy().set_opacity(1)
                
                self.play(
                    ReplacementTransform(g_dots1, target_copy),
                    FadeOut(g_dots2), FadeOut(g_dots3),
                    run_time=0.8
                )
                self.remove(target_copy)
                
                # CHÌA KHÓA CHỐNG MẤT TÍCH: Bật sáng và THÊM VÀO SCENE
                target_group.set_opacity(1)
                self.add(target_group)
            else:
                g_s = MathTex(eq_bottom[target_indices[0]].get_tex_string(), font_size=45).set_color(C_SIGMA)
                g_u = MathTex(eq_bottom[target_indices[1]].get_tex_string(), font_size=45).set_color(C_U)
                g_v = MathTex(eq_bottom[target_indices[2]].get_tex_string(), font_size=45).set_color(C_V)
                ghost_group = VGroup(g_s, g_u, g_v).arrange(RIGHT, buff=0.1).move_to(DOWN * 0.8)
                
                self.play(
                    TransformFromCopy(s_mob, g_s),
                    TransformFromCopy(u_mob, g_u),
                    TransformFromCopy(v_mob, g_v),
                    run_time=1.2
                )
                self.wait(0.3)
                
                target_group = VGroup(*[eq_bottom[i] for i in target_indices])
                target_copy = target_group.copy().set_opacity(1)
                
                self.play(
                    Transform(ghost_group, target_copy),
                    run_time=0.8
                )
                self.remove(ghost_group, target_copy)
                
                # CHÌA KHÓA CHỐNG MẤT TÍCH
                for i in target_indices:
                    eq_bottom[i].set_opacity(1)
                    self.add(eq_bottom[i]) 
                    
            self.wait(0.5)

        # --- 7. CHẠY CÁC BƯỚC ---
        # BƯỚC 1
        execute_step(0, 0, [4, 5, 6])
        
        # BƯỚC 2: Di chuyển khung (Không hiện dấu cộng)
        self.play(
            rect_u.animate.become(get_u_box(1)),
            rect_s.animate.become(get_s_box(5)),
            rect_v.animate.become(get_v_box(1))
        )
        execute_step(1, 5, [8, 9, 10])
        
        # BƯỚC 3 (DẤU ...): Di chuyển khung đến dấu ... và đem dấu ... xuống
        self.play(
            rect_u.animate.become(get_u_box(2)),
            rect_s.animate.become(get_s_box(10)),
            rect_v.animate.become(get_v_box(2))
        )
        execute_step(2, 10, [12], is_dots=True)
        
        # BƯỚC 4 (Thành phần n)
        self.play(
            rect_u.animate.become(get_u_box(3)),
            rect_s.animate.become(get_s_box(15)),
            rect_v.animate.become(get_v_box(3))
        )
        execute_step(3, 15, [14, 15, 16])
        
        # --- 8. OUTRO: UNCREATE KHUNG & LẦN LƯỢT HIỆN DẤU CỘNG ---
        # Phải set opacity về 1 trước khi dùng FadeIn/Write
        eq_bottom[7].set_opacity(1)
        eq_bottom[11].set_opacity(1)
        eq_bottom[13].set_opacity(1)
        
        self.play(
            Uncreate(rect_u), Uncreate(rect_s), Uncreate(rect_v),
            AnimationGroup(
                Write(eq_bottom[7]),   # + thứ 1
                Write(eq_bottom[11]),  # + thứ 2
                Write(eq_bottom[13]),  # + thứ 3
                lag_ratio=0.3
            ),
            run_time=2
        )
        
        # Chắc chắn add toàn bộ dấu cộng vào Scene để kết thúc đẹp
        self.add(eq_bottom[7], eq_bottom[11], eq_bottom[13])
        self.wait(2)

        


        # =====================================================================
        # 9. CHUYỂN CẢNH: RÚT MA TRẬN, ĐẨY BIỂU THỨC LÊN TRÊN (Ảnh 4)
        # =====================================================================
        # Ẩn các phần tử ma trận phía trên (Bao gồm các vector, ma trận Sigma và các dấu ngoặc)
        self.play(
            FadeOut(mat_S), FadeOut(vec_u_list), FadeOut(vec_v_list),
            FadeOut(mat_U_exp.get_brackets()), FadeOut(mat_V_exp.get_brackets()),
            run_time=1.5
        )
        
        # Di chuyển phương trình từ dưới đáy lên sát đường kẻ ngang
        self.play(
            eq_bottom.animate.next_to(line, DOWN, buff=0.5),
            run_time=1.5
        )
        self.wait(1)

        # --- 2. HIỆN TỪ TỪ VECTOR U VÀ V BẰNG HIỆU ỨNG WRITE (VẼ CHỮ) ---
        
        # Setup Vector U
        u_matrix = Matrix([["u_{1i}"], ["u_{2i}"], ["\\vdots"], ["u_{ni}"]], v_buff=0.9).set_color(C_U)
        u_matrix.get_entries()[2].set_color(WHITE)
        u_matrix.move_to(DOWN * 2 + LEFT * 3.5)
        
        u_brackets = u_matrix.get_brackets().set_color(WHITE)
        u_entries = u_matrix.get_entries()
        u_lbl = MathTex("\\vec{u}_i", "=", font_size=40).set_color(C_U).next_to(u_matrix, LEFT)

        # Animation U
        self.play(Write(u_lbl), run_time=0.8)
        self.play(Write(u_brackets[0]), run_time=0.4)
        
        # Đã đổi FadeIn thành Write để các phần tử hiện ra như đang được viết
        self.play(
            AnimationGroup(*[Write(entry) for entry in u_entries], lag_ratio=0.4), 
            run_time=1.5
        )
        
        self.play(Write(u_brackets[1]), run_time=0.4)
        self.wait(0.5)

        # Setup Vector V
        v_matrix = Matrix([["v_{1i}", "v_{2i}", "\\dots", "v_{ni}"]], h_buff=1.5).set_color(C_V)
        v_matrix.get_entries()[2].set_color(WHITE) 
        v_matrix.move_to(UP * 0.5 + RIGHT * 1.5)
        
        v_brackets = v_matrix.get_brackets().set_color(WHITE)
        v_entries = v_matrix.get_entries()
        v_lbl = MathTex("\\vec{v}_i^\\top", "=", font_size=40).set_color(C_V).next_to(v_matrix, LEFT)

        # Animation V
        self.play(Write(v_lbl), run_time=0.8)
        self.play(Write(v_brackets[0]), run_time=0.4)
        
        # Đã đổi FadeIn thành Write
        self.play(
            AnimationGroup(*[Write(entry) for entry in v_entries], lag_ratio=0.4), 
            run_time=1.5
        )
        
        self.play(Write(v_brackets[1]), run_time=0.4)
        self.wait(1)

        # --- 3. HIỆU ỨNG ĐẨY NỐI TIẾP NHAU (CASCADING) ---
        u_texts = ["u_{1i}", "u_{2i}", "", "u_{ni}"]
        v_texts = ["v_{1i}", "v_{2i}", "", "v_{ni}"]
        
        u_mobs = [[None for _ in range(4)] for _ in range(4)]
        v_mobs = [[None for _ in range(4)] for _ in range(4)]
        dots_mobs = []
        result_group = VGroup()
        
        for i in range(4):     
            for j in range(4): 
                target_pos = np.array([v_entries[j].get_x(), u_entries[i].get_y(), 0])
                
                if i == 2 and j == 2:
                    dots = MathTex("\\ddots", font_size=38).move_to(target_pos)
                    dots_mobs.append(dots)
                    result_group.add(dots)
                elif i == 2:
                    dots = MathTex("\\vdots", font_size=38).move_to(target_pos)
                    dots_mobs.append(dots)
                    result_group.add(dots)
                elif j == 2:
                    dots = MathTex("\\dots", font_size=38).move_to(target_pos)
                    dots_mobs.append(dots)
                    result_group.add(dots)
                else:
                    g_u = MathTex(u_texts[i], font_size=38).set_color(C_U)
                    g_v = MathTex(v_texts[j], font_size=38).set_color(C_V)
                    target_mob = VGroup(g_u, g_v).arrange(RIGHT, buff=0.1).move_to(target_pos)
                    
                    u_mobs[i][j] = g_u
                    v_mobs[i][j] = g_v
                    result_group.add(target_mob)

        valid_idx = [0, 1, 3] 
        
        anim_step1 = []
        for i in valid_idx: anim_step1.append(TransformFromCopy(u_entries[i], u_mobs[i][0]))
        for j in valid_idx: anim_step1.append(TransformFromCopy(v_entries[j], v_mobs[0][j]))
        self.play(*anim_step1, run_time=0.7)

        anim_step2 = []
        for i in valid_idx: anim_step2.append(TransformFromCopy(u_mobs[i][0], u_mobs[i][1]))
        for j in valid_idx: anim_step2.append(TransformFromCopy(v_mobs[0][j], v_mobs[1][j]))
        self.play(*anim_step2, run_time=0.7)

        anim_step3 = [FadeIn(dot) for dot in dots_mobs]
        for i in valid_idx: anim_step3.append(TransformFromCopy(u_mobs[i][1], u_mobs[i][3]))
        for j in valid_idx: anim_step3.append(TransformFromCopy(v_mobs[1][j], v_mobs[3][j]))
        self.play(*anim_step3, run_time=0.8)

        # --- 4. HOÀN THIỆN KẾT QUẢ VỚI NGOẶC MATRIX CHUẨN ---
        left_bracket = u_matrix.get_brackets()[0].copy().set_color(WHITE)
        right_bracket = u_matrix.get_brackets()[1].copy().set_color(WHITE)
        
        left_bracket.next_to(result_group, LEFT, buff=0.2)
        right_bracket.next_to(result_group, RIGHT, buff=0.2)

        eq_final = MathTex("=", "\\vec{u}_i", "\\vec{v}_i^\\top", font_size=45)
        eq_final[1].set_color(C_U)
        eq_final[2].set_color(C_V)
        eq_final.next_to(right_bracket, RIGHT, buff=0.3)

        self.play(
            Write(left_bracket), 
            Write(right_bracket),
            FadeIn(eq_final)
        )
        self.wait(2)



        # =====================================================================
        # --- CHUYỂN CẢNH MƯỢT ĐỂ GHÉP NỐI 2 PHẦN ---
        # =====================================================================
        # Gom tất cả các object đang hiển thị trên màn hình lại
        current_mobjects = Group(*self.mobjects)
        
        # Xóa sạch màn hình với hiệu ứng mờ dần và trượt nhẹ xuống dưới
        self.play(
            FadeOut(current_mobjects, shift=DOWN * 0.5), 
            run_time=1.5
        )
        self.wait(0.5)

        # --- 1. ĐỌC ẢNH VÀ TÍNH TOÁN SVD THỰC TẾ ---
        img_path = "image2.jpg"
        try:
            img_pil = Image.open(img_path).convert('L')
            # Thumbnail nhỏ hơn để Manim render mượt, đảm bảo ảnh đen trắng 'L'
            img_pil.thumbnail((200, 200)) 
            img_array = np.array(img_pil)
        except FileNotFoundError:
            # Sinh mảng nhiễu ngẫu nhiên nếu không tìm thấy file để tránh crash
            img_array = np.random.randint(0, 255, (64, 64), dtype=np.uint8)

        # Tính SVD bằng Numpy: A = U * S * V^T
        U, S, V = np.linalg.svd(img_array, full_matrices=False)

        # Tạo ImageMobject cho ảnh gốc (Mảng 3 kênh RGB cho Manim)
        orig_rgb = np.stack((img_array.astype(np.uint8),)*3, axis=-1)
        
        # --- ĐIỀU CHỈNH 1: Ảnh bên trái nhỏ lại và dịch qua trái ---
        original_image = ImageMobject(orig_rgb)
        # 1.1 Tỉ lệ ảnh gốc nhỏ lại (từ 4.5 xuống 3.0)
        original_image.scale_to_fit_height(3.5)
        # 1.2 Dịch qua trái nhiều hơn (buff nhỏ hơn từ 0.8 xuống 0.5)
        original_image.to_edge(LEFT, buff=0.65)
        
        # Viền trắng bao quanh ảnh gốc
        original_border = Rectangle(width=original_image.width, height=original_image.height, color=WHITE, stroke_width=3)
        original_border.move_to(original_image)
        original_group = Group(original_image, original_border)

        # --- ĐIỀU CHỈNH 2: Làm dấu toán học nhỏ lại một chút ---
        equals_sign = MathTex("=", font_size=60).next_to(original_group, RIGHT, buff=0.3)
        sum_sign = MathTex("\\sum", font_size=90).next_to(equals_sign, RIGHT, buff=0.3)

        # --- 3. CHUẨN BỊ LƯỚI THÀNH PHẦN TỪ SVD ---
        # Tách riêng các nhóm để làm hiệu ứng nối tiếp nhau
        images_grid = Group()    # Chỉ chứa ảnh và viền
        overlays_group = Group() # Chỉ chứa kính mờ
        texts_group = VGroup()   # Chỉ chứa chữ toán học

        num_rows, num_cols = 4, 4
        
        # --- ĐIỀU CHỈNH 3: Lưới ảnh to hơn và khít hơn ---
        # 3.1 Tăng tỉ lệ ảnh thành phần (từ 1.0 lên 1.5)
        cell_height = 1.63
        # 3.2 Giảm buff giữa các ô để lưới khít hơn (từ 0.15 xuống 0.1)
        cell_buff = 0.1 

        for i in range(num_rows):
            for j in range(num_cols):
                index = i * num_cols + j
                
                # Tính toán ma trận thành phần rank-1
                comp_matrix = S[index] * np.outer(U[:, index], V[index, :])
                
                # Chuẩn hóa ma trận về dải pixel [0, 255]
                c_min, c_max = comp_matrix.min(), comp_matrix.max()
                if c_max - c_min > 1e-8:
                    comp_norm = 255 * (comp_matrix - c_min) / (c_max - c_min)
                else:
                    comp_norm = np.zeros_like(comp_matrix)
                    
                # Tạo ImageMobject từ ma trận đen trắng
                comp_rgb = np.stack((comp_norm.astype(np.uint8),)*3, axis=-1)
                comp_img = ImageMobject(comp_rgb).scale_to_fit_height(cell_height)
                
                # Viền trắng bao quanh mỗi ô nhỏ
                comp_border = Rectangle(width=comp_img.width, height=comp_img.height, color=WHITE, stroke_width=1.5)
                comp_border.move_to(comp_img)
                
                # Thêm vào nhóm Ảnh
                cell_img_group = Group(comp_img, comp_border)
                images_grid.add(cell_img_group)
                
                # Kính mờ (chưa định vị) để chữ đè lên dễ đọc
                overlay = Rectangle(width=comp_img.width, height=comp_img.height, color=BLACK, fill_opacity=0.2, stroke_width=0)
                overlays_group.add(overlay)
                
                # Chữ toán học 2 dòng (chưa định vị), font size to hơn chút để cân đối
                tex1 = MathTex(f"\\vec{{u}}_{{{index}}}", f"\\vec{{v}}_{{{index}}}^\\top", font_size=45)
                tex1[0].set_color(C_U)
                tex1[1].set_color(C_V)
                tex2 = MathTex("\\times", f"\\sigma_{{{index}}}", font_size=45)
                tex2[0].set_color(WHITE)
                tex2[1].set_color(C_SIGMA)
                text_group = VGroup(tex1, tex2).arrange(DOWN, buff=0.1)

                text_group.set_stroke(color=BLACK, width=6, background=True)
                
                texts_group.add(text_group)

        # Xếp nhóm ảnh thành lưới 4x4 và đặt vị trí bên phải dấu Tổng
        images_grid.arrange_in_grid(rows=num_rows, cols=num_cols, buff=cell_buff)
        # Giảm buff để dịch qua trái nhiều hơn (từ 0.5 xuống 0.3)
        images_grid.next_to(sum_sign, RIGHT, buff=0.3)

        # Khớp tọa độ của kính mờ và chữ theo tọa độ của ảnh vừa được xếp lưới
        for cell, overlay, text in zip(images_grid, overlays_group, texts_group):
            overlay.move_to(cell)
            text.move_to(cell)

        # --- 4. HOẠT ẢNH THEO KỊCH BẢN (TIMELINE MỚI) ---
        
        # BƯỚC 1: Chỉ hiện ảnh gốc
        self.add(original_group)
        self.wait(1)
        
        # BƯỚC 2: Phân rã FIRST - Các ảnh thành phần (Rank-1) bay ra từ tâm ảnh gốc
        # Hiệu ứng này bay từ tâm ảnh gốc tỏa tứ phía ra vị trí đích
        origin_center = original_group.get_center()
        fly_out_animations = []
        for cell in images_grid:
            # Khoảng cách từ tâm ảnh gốc đến vị trí đích của ô đó
            vector_shift = cell.get_center() - origin_center
            
            # FadeIn ô ảnh với hiệu ứng Shift, tức là ô ảnh bắt đầu tại origin_center
            # và lướt về vị trí cell.get_center() (lag_ratio để nối đuôi nhau)
            fly_out_animations.append(FadeIn(cell, shift=vector_shift))

        self.play(
            AnimationGroup(*fly_out_animations, lag_ratio=0.1), 
            run_time=8,
            rate_func=smooth
        )
        self.wait(1)

        # BƯỚC 3: CHỜ lưới tách hết, then dấu = Σ xuất hiện
        self.play(FadeIn(equals_sign), FadeIn(sum_sign))
        self.wait(1)

        # BƯỚC 4: Cuối cùng là phủ kính mờ và viết công thức lên từng ảnh thành phần
        self.play(FadeIn(overlays_group, run_time=1))
        
        # Viết công thức nối đuôi nhau
        self.play(
            AnimationGroup(*[Write(text) for text in texts_group], lag_ratio=0.2),
            run_time=3
        )
        
        self.wait(3)

# Đoạn video số 6
class LowRankTheory(Scene):
    def construct(self):
        # 1. TIÊU ĐỀ CHÍNH
        title_vn = Text("Xấp xỉ hạng thấp & Tỉ lệ lưu trữ", font=VN_FONT, weight=BOLD, font_size=40)
        title_vn.to_edge(UP, buff=0.5)
        self.play(Write(title_vn))
        self.wait(0.5)

        # 2. CÔNG THỨC XẤP XỈ HẠNG k
        subtitle_approx = Text("Công thức xấp xỉ tốt nhất hạng k:", font=VN_FONT, font_size=28, color=BLUE_A)
        subtitle_approx.next_to(title_vn, DOWN, buff=0.6)
        
        # TỰ ĐỘNG MAP THEO MÀU GLOBAL CỦA BẠN
        formula_approx = MathTex(
            r"A_k = \sum_{i=1}^k \sigma_i \mathbf{u}_i \mathbf{v}_i^T",
            tex_to_color_map={
                r"\sigma_i": C_SIGMA,
                r"\mathbf{u}_i": C_U,
                r"\mathbf{v}_i^T": C_V,
            },
            font_size=44
        )
        formula_approx.next_to(subtitle_approx, DOWN, buff=0.3)

        self.play(FadeIn(subtitle_approx, shift=DOWN))
        self.play(Write(formula_approx))
        self.wait(1)

        # 3. PHÂN TÍCH KHÔNG GIAN LƯU TRỮ
        subtitle_storage = Text("Phân tích không gian lưu trữ:", font=VN_FONT, font_size=28, color=BLUE_A)
        subtitle_storage.next_to(formula_approx, DOWN, buff=0.8)

        item_1 = VGroup(
            Text("• Ảnh gốc (Ma trận", font=VN_FONT, font_size=24),
            MathTex(r"{{m}} \times {{n}}", font_size=30),
            Text("):", font=VN_FONT, font_size=24)
        ).arrange(RIGHT, buff=0.15) 
        
        item_1[1].set_color_by_tex("m", BLUE_C)
        item_1[1].set_color_by_tex("n", GREEN_C)
        
        u_comma = MathTex(r"\mathbf{u}_i", ",", font_size=30)
        u_comma[0].set_color(C_U)
        
        sigma_comma = MathTex(r"\sigma_i", ",", font_size=30)
        sigma_comma[0].set_color(C_SIGMA)

        item_2 = VGroup(
            Text("• Ma trận hạng", font=VN_FONT, font_size=24),
            MathTex("k", font_size=30, color=YELLOW),
            Text("cần lưu:", font=VN_FONT, font_size=24),
            MathTex("k", font_size=30, color=YELLOW),
            Text("cột", font=VN_FONT, font_size=24),
            u_comma,
            MathTex("k", font_size=30, color=YELLOW),
            Text("giá trị", font=VN_FONT, font_size=24),
            sigma_comma,
            MathTex("k", font_size=30, color=YELLOW),
            Text("dòng", font=VN_FONT, font_size=24),
            MathTex(r"\mathbf{v}_i^T", font_size=30, color=C_V)
        ).arrange(RIGHT, buff=0.15) 
        
        item_1[1].shift(DOWN * 0.05)
        for mob in item_2:
            if isinstance(mob, MathTex):
                mob.shift(DOWN * 0.05)

        storage_details = VGroup(item_1, item_2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        storage_details.next_to(subtitle_storage, DOWN, buff=0.3)
        
        math_storage_1 = MathTex(r"{{k}} \cdot {{m}} + {{k}} + {{k}} \cdot {{n}}", font_size=32)
        math_storage_2 = MathTex("=", font_size=32)
        math_storage_3 = MathTex(r"{{k}}( {{m}} + {{n}} + 1)", font_size=32)

        formula_storage = VGroup(
            Text("Tổng dữ liệu = ", font=VN_FONT, font_size=26),
            math_storage_1, math_storage_2, math_storage_3
        ).arrange(RIGHT, buff=0.2)
        
        for mob in formula_storage[1:]:
            mob.shift(DOWN * 0.05)
            
        for tex_mob in [math_storage_1, math_storage_3]:
            tex_mob.set_color_by_tex("k", YELLOW)
            tex_mob.set_color_by_tex("m", BLUE_C)
            tex_mob.set_color_by_tex("n", GREEN_C)

        formula_storage.next_to(storage_details, DOWN, buff=0.4)

        self.play(FadeIn(subtitle_storage, shift=DOWN))
        self.play(FadeIn(storage_details[0], shift=RIGHT))
        self.play(FadeIn(storage_details[1], shift=RIGHT))
        self.play(Write(formula_storage))
        self.wait(1)

        # 4. CHUYỂN CẢNH: ĐÓNG KHUNG ĐỒNG THỜI VÀ BIẾN ĐỔI THÀNH PHÂN SỐ
        box_num = SurroundingRectangle(math_storage_3, color=YELLOW, buff=0.2)
        box_den = SurroundingRectangle(item_1[1], color=YELLOW, buff=0.2)
        
        self.play(
            title_vn.animate.set_opacity(0.2),
            subtitle_approx.animate.set_opacity(0.2),
            formula_approx.animate.set_opacity(0.2),
            subtitle_storage.animate.set_opacity(0.2),
            item_2.animate.set_opacity(0.2),
            formula_storage[0:3].animate.set_opacity(0.2),
            item_1[0].animate.set_opacity(0.2),
            item_1[2].animate.set_opacity(0.2),
            Create(box_num),
            Create(box_den),
            run_time=1.5
        )
        self.wait(0.5)
        
        numerator = MathTex(r"{{k}}( {{m}} + {{n}} + 1)", font_size=40)
        numerator.set_color_by_tex("k", YELLOW)
        numerator.set_color_by_tex("m", BLUE_C)
        numerator.set_color_by_tex("n", GREEN_C)

        denominator = MathTex(r"{{m}} \times {{n}}", font_size=40)
        denominator.set_color_by_tex("m", BLUE_C)
        denominator.set_color_by_tex("n", GREEN_C)

        frac_line = Line(LEFT, RIGHT).set_width(max(numerator.width, denominator.width) + 0.2)
        fraction_group = VGroup(numerator, frac_line, denominator).arrange(DOWN, buff=0.15)
        
        formula_ratio = VGroup(
            Text("Tỉ lệ lưu trữ =", font=VN_FONT, font_size=36, color=GREEN_B),
            fraction_group
        ).arrange(RIGHT, buff=0.3)
        formula_ratio.move_to(ORIGIN) 

        self.play(
            FadeOut(title_vn), FadeOut(subtitle_approx), FadeOut(formula_approx),
            FadeOut(subtitle_storage), FadeOut(item_2), 
            FadeOut(formula_storage[0:3]), 
            FadeOut(item_1[0]), FadeOut(item_1[2]), 
            FadeOut(box_num), FadeOut(box_den),
            
            Write(formula_ratio[0]), 
            Create(frac_line),
            
            ReplacementTransform(math_storage_3, numerator),
            ReplacementTransform(item_1[1], denominator),
            run_time=2
        )
        self.wait(2)

        self.play(
            formula_ratio.animate.scale(1.2),
            run_time=1
        )
        self.wait(1)
        self.play(FadeOut(formula_ratio))


# Đoạn video số 7
class SVDImageCompression(Scene):
    def construct(self):
        # Thiết lập font chữ
        VN_FONT = "Arial"
        
        # =====================================================================
        # 1. ĐỌC ẢNH VÀ PHÂN RÃ SVD
        # =====================================================================
        img_filename = "image.jpg"
        
        if os.path.exists(img_filename):
            pil_img = Image.open(img_filename).convert('L')
            pil_img = pil_img.resize((300, 300))
        else:
            arr = np.linspace(0, 255, 300*300).reshape(300, 300)
            pil_img = Image.fromarray(arr.astype(np.uint8))

        img_array = np.array(pil_img)
        h, w = img_array.shape
        k_max = min(h, w)
        
        U, S, Vt = np.linalg.svd(img_array, full_matrices=False)

        # =====================================================================
        # 2. KHỞI TẠO BỐ CỤC UI TRÊN MÀN HÌNH
        # =====================================================================
        title = Text("SVD: Tổng các ma trận hạng 1 (Rank-1 Matrices)", font=VN_FONT, font_size=36, color=BLUE_B).to_edge(UP)
        self.play(Write(title))
        
        txt_left = Text("Ảnh xấp xỉ Rank k", font=VN_FONT, font_size=24, color=YELLOW).move_to(LEFT * 3.5 + UP * 2.5)
        txt_right = Text("Layer k (Thành phần)", font=VN_FONT, font_size=24, color=GREEN).move_to(RIGHT * 3.5 + UP * 2.5)
        self.play(FadeIn(txt_left), FadeIn(txt_right))
        
        frame_left = SurroundingRectangle(
            Group(ImageMobject(np.zeros((h,w,3))).set_height(4.5).move_to(LEFT * 3.5)), 
            color=WHITE, buff=0
        )
        frame_right = SurroundingRectangle(
            Group(ImageMobject(np.zeros((h,w,3))).set_height(4.5).move_to(RIGHT * 3.5)), 
            color=GRAY, buff=0
        )
        self.play(Create(frame_left), Create(frame_right))

        current_left_img = ImageMobject(np.zeros((h, w, 3), dtype=np.uint8)).set_height(4.5).move_to(LEFT * 3.5)
        self.add(current_left_img)
        
        current_k_text = Text("Rank k = 0", font=VN_FONT, font_size=24, color=YELLOW).next_to(frame_left, DOWN)
        current_ratio_text = Text("Dung lượng: 0%", font=VN_FONT, font_size=20, color=LIGHT_GRAY).next_to(current_k_text, DOWN)
        self.add(current_k_text, current_ratio_text)




        # =====================================================================
        # 3. THỰC THI HOẠT ẢNH CỘNG DỒN TỪNG LAYER
        # =====================================================================
        accumulated_matrix = np.zeros((h, w))
        prev_k = 0
        
        # --- GIAI ĐOẠN 1 & 2: RỜI RẠC (Từ k=1 đến k=20) ---
        for k in range(1, 21):
            # Điều chỉnh tốc độ: Chậm rãi ở 1-10, nhanh hơn một chút ở 11-20
            speed_factor = 1.0 if k <= 10 else 0.5

            layer_matrix = np.zeros((h, w))
            for i in range(prev_k, k):
                layer_matrix += S[i] * np.outer(U[:, i], Vt[i, :])
            
            max_abs = np.max(np.abs(layer_matrix))
            if max_abs == 0: max_abs = 1
            layer_vis = np.clip((layer_matrix / max_abs) * 127 + 127, 0, 255).astype(np.uint8)
            
            # Chập 3 kênh để sửa lỗi nhòe/bóng ma của Manim
            layer_vis_rgb = np.stack((layer_vis, layer_vis, layer_vis), axis=-1)
            right_img = ImageMobject(layer_vis_rgb).set_height(4.5).move_to(RIGHT * 3.5)
            
            layer_text = Text(f"Layer {k}", font=VN_FONT, font_size=20, color=WHITE).next_to(frame_right, DOWN)
            
            # Khung phải hiện ra
            self.play(FadeIn(right_img), Write(layer_text), run_time=0.8 * speed_factor)
            self.wait(0.5 * speed_factor)
            
            # Bay sang khung trái
            self.play(
                right_img.animate.move_to(LEFT * 3.5), 
                FadeOut(layer_text),
                run_time=1.2 * speed_factor
            )
            
            # Cập nhật ảnh cộng dồn bên trái
            accumulated_matrix += layer_matrix
            acc_vis = np.clip(accumulated_matrix, 0, 255).astype(np.uint8)
            acc_vis_rgb = np.stack((acc_vis, acc_vis, acc_vis), axis=-1)
            
            new_left_img = ImageMobject(acc_vis_rgb).set_height(4.5).move_to(LEFT * 3.5)
            new_left_img.set_z_index(current_left_img.get_z_index() + 1)
            
            k_text = Text(f"Rank k = {k}", font=VN_FONT, font_size=24, color=YELLOW).next_to(frame_left, DOWN)
            ratio = (k * (h + w + 1)) / (h * w) * 100
            ratio_text = Text(f"Tỷ lệ lưu trữ: {ratio:.1f}%", font=VN_FONT, font_size=20, color=LIGHT_GRAY).next_to(k_text, DOWN)
            
            self.play(
                FadeIn(new_left_img, run_time=0.8 * speed_factor),
                ReplacementTransform(current_k_text, k_text, run_time=0.6 * speed_factor),
                ReplacementTransform(current_ratio_text, ratio_text, run_time=0.6 * speed_factor)
            )
            
            self.remove(current_left_img, right_img)
            
            current_left_img = new_left_img
            current_k_text = k_text
            current_ratio_text = ratio_text
            prev_k = k
            
            self.wait(0.5 * speed_factor)

        self.wait(1)

        # --- GIAI ĐOẠN 3: LIÊN TỤC (Từ k=20 đến k=150) ---
        txt_fast = Text("Tăng tốc nén dữ liệu...", font=VN_FONT, font_size=24, color=GREEN).next_to(frame_right, DOWN)
        self.play(Write(txt_fast))
        self.wait(1.5)
        self.play(FadeOut(txt_fast))

        k_tracker = ValueTracker(20)

        # Cập nhật ảnh cộng dồn (Bên trái)
        def get_continuous_compressed():
            k_val = int(k_tracker.get_value())
            k_val = min(max(k_val, 1), k_max)
            recon = U[:, :k_val] @ np.diag(S[:k_val]) @ Vt[:k_val, :]
            res = np.clip(recon, 0, 255).astype(np.uint8)
            res_rgb = np.stack((res,)*3, axis=-1)
            return ImageMobject(res_rgb).set_height(4.5).move_to(LEFT * 3.5)

        # Cập nhật thành phần Layer hiện tại (Bên phải - không bay sang trái nữa)
        def get_continuous_layer():
            k_val = int(k_tracker.get_value())
            k_val = min(max(k_val, 1), k_max)
            idx = k_val - 1
            # Chỉ lấy đúng 1 layer thứ k
            single_layer = S[idx] * np.outer(U[:, idx], Vt[idx, :])
            max_ab = np.max(np.abs(single_layer))
            if max_ab == 0: max_ab = 1
            l_vis = np.clip((single_layer / max_ab) * 127 + 127, 0, 255).astype(np.uint8)
            l_vis_rgb = np.stack((l_vis,)*3, axis=-1)
            return ImageMobject(l_vis_rgb).set_height(4.5).move_to(RIGHT * 3.5)

        # Đăng ký always_redraw
        continuous_left_img = always_redraw(get_continuous_compressed)
        continuous_right_img = always_redraw(get_continuous_layer)
        
        continuous_rank_txt = always_redraw(lambda: Text(
            f"Rank k = {int(k_tracker.get_value())}", font=VN_FONT, font_size=24, color=YELLOW
        ).next_to(frame_left, DOWN))
        
        continuous_ratio_txt = always_redraw(lambda: Text(
            f"Dung lượng: {(int(k_tracker.get_value())*(h+w+1))/(h*w)*100:.1f}%", 
            font=VN_FONT, font_size=20, color=LIGHT_GRAY
        ).next_to(continuous_rank_txt, DOWN))
        
        continuous_layer_txt = always_redraw(lambda: Text(
            f"Layer {int(k_tracker.get_value())}", font=VN_FONT, font_size=20, color=WHITE
        ).next_to(frame_right, DOWN))

        # Thay thế mobject tĩnh bằng mobject động
        self.add(continuous_left_img, continuous_right_img, continuous_rank_txt, continuous_ratio_txt, continuous_layer_txt)
        self.remove(current_left_img, current_k_text, current_ratio_text)

        # Chạy mượt từ 20 đến 150 với tốc độ vừa phải (10 giây)
        self.play(k_tracker.animate.set_value(150), run_time=10, rate_func=linear)
        self.wait(2)

        k_target = 150
        target_matrix = U[:, :k_target] @ np.diag(S[:k_target]) @ Vt[:k_target, :]
        
        # Dọn dẹp Text chuẩn bị vào Đồ thị
        self.play(FadeOut(
            continuous_left_img, continuous_right_img, 
            continuous_rank_txt, continuous_ratio_txt, continuous_layer_txt, 
            txt_left, txt_right, title
        ))



        # =====================================================================
        # 4. PHÂN TÍCH ĐỒ THỊ SINGULAR VALUES
        # =====================================================================
        self.play(
            FadeOut(title), FadeOut(txt_left), FadeOut(txt_right), 
            FadeOut(frame_right)
        )
        
        max_log = int(np.ceil(np.log10(S[0]))) 
        if max_log < 3: max_log = 3 
        min_log = -3 
        
        chart = Axes(
            x_range=[0, k_max + 1, k_max // 5], 
            y_range=[min_log, max_log, 1],
            x_length=6,
            y_length=4.5,
            axis_config={"color": WHITE, "include_numbers": False}
        ).move_to(RIGHT * 3.5)

        k_target = int(k_max * 0.15) 

        bg_left = Polygon(
            chart.c2p(0, min_log), chart.c2p(k_target, min_log),
            chart.c2p(k_target, max_log), chart.c2p(0, max_log),
            fill_color="#0D2A31", fill_opacity=1, stroke_width=0
        )
        bg_right = Polygon(
            chart.c2p(k_target, min_log), chart.c2p(k_max, min_log),
            chart.c2p(k_max, max_log), chart.c2p(k_target, max_log),
            fill_color="#5D2D2A", fill_opacity=1, stroke_width=0
        )
        
        grid_lines = VGroup()
        for x in range(0, k_max + 1, k_max // 5):
            grid_lines.add(Line(chart.c2p(x, min_log), chart.c2p(x, max_log), color=GRAY, stroke_width=1, stroke_opacity=0.6))
            
        for y in range(min_log, max_log + 1):
            grid_lines.add(Line(chart.c2p(0, y), chart.c2p(k_max, y), color=WHITE, stroke_width=1, stroke_opacity=0.4))
            for m in range(2, 10):
                minor_y = np.log10(10**y * m)
                if minor_y <= max_log:
                    grid_lines.add(Line(chart.c2p(0, minor_y), chart.c2p(k_max, minor_y), color=GRAY, stroke_width=0.5, stroke_opacity=0.3))

        chart_frame = Polygon(
            chart.c2p(0, min_log), chart.c2p(k_max, min_log),
            chart.c2p(k_max, max_log), chart.c2p(0, max_log),
            color=WHITE, stroke_width=2
        )

        y_labels = VGroup()
        for y in range(min_log, max_log + 1):
            val = 10**y
            text_val = f"{int(val)}" if val >= 1 else f"{val}"
            y_labels.add(Text(text_val, font=VN_FONT, font_size=16, color=WHITE).next_to(chart.c2p(0, y), LEFT, buff=0.15))
        
        x_labels = VGroup()
        for x in range(0, k_max + 1, k_max // 5):
            x_labels.add(Text(str(x), font=VN_FONT, font_size=16, color=WHITE).next_to(chart.c2p(x, min_log), DOWN, buff=0.15))

        # Thêm nhãn rõ ràng cho các trục đồ thị
        x_axis_label = Text("Chỉ số k", font=VN_FONT, font_size=20, color=YELLOW).next_to(chart_frame, DOWN, buff=0.6)
        y_axis_label = VGroup(
            Text("Giá trị ", font=VN_FONT, font_size=20, color=BLUE_B),
            MathTex(r"\sigma_k", color=BLUE_B)
        ).arrange(RIGHT, buff=0.1).next_to(chart_frame, UP, buff=0.2)

        points_3d = []
        for i in range(k_max):
            k = i + 1
            val = S[i]
            if val > 0:
                y_val = np.log10(val)
            else:
                y_val = min_log
            y_clamped = max(y_val, min_log)
            points_3d.append(chart.c2p(k, y_clamped))

        graph_line = VMobject(color="#A8C4D6", stroke_width=3)
        graph_line.set_points_as_corners(points_3d)

        title_graph = Text(f"Cắt tại k = {k_target} (Dung lượng: {((k_target * (h + w + 1)) / (h * w) * 100):.1f}%)", font=VN_FONT, font_size=32, color=YELLOW).to_edge(UP)

        self.play(
            FadeIn(bg_left), FadeIn(bg_right), 
            Create(grid_lines), Create(chart_frame),
            Write(y_labels), Write(x_labels), Write(title_graph),
            Write(x_axis_label), Write(y_axis_label)
        )
        self.play(Create(graph_line), run_time=2)

        target_matrix = np.zeros((h, w))
        for i in range(k_target):
            target_matrix += S[i] * np.outer(U[:, i], Vt[i, :])
        target_vis = np.clip(target_matrix, 0, 255).astype(np.uint8)
        target_vis_rgb = np.stack((target_vis, target_vis, target_vis), axis=-1)
        
        img_target = ImageMobject(target_vis_rgb).set_height(4.5).move_to(LEFT * 3.5)
        
        k_text_target = Text(f"Rank k = {k_target}", font=VN_FONT, font_size=24, color=YELLOW).next_to(frame_left, DOWN)
        ratio_target = Text(f"Dung lượng: {((k_target * (h + w + 1)) / (h * w) * 100):.1f}%", font=VN_FONT, font_size=20, color=LIGHT_GRAY).next_to(k_text_target, DOWN)
        
        self.play(
            FadeIn(img_target), FadeOut(current_left_img),
            ReplacementTransform(current_k_text, k_text_target),
            ReplacementTransform(current_ratio_text, ratio_target)
        )
        self.wait(2)


        # =====================================================================
        # 5. SO SÁNH TRỰC DIỆN, ZOOM, VÀ KẾT LUẬN TRÊN ĐỒ THỊ
        # =====================================================================
        
        # --- 5.1. Phủ màn đen lên đồ thị và hiện Ảnh Gốc bên phải ---
        dim_overlay = Rectangle(
            width=7, height=6, color=BLACK, fill_opacity=0.85
        ).move_to(chart.get_center())

        img_array_rgb = np.stack((img_array, img_array, img_array), axis=-1)
        img_original = ImageMobject(img_array_rgb).set_height(4.5).move_to(RIGHT * 3.5)
        
        k_text_orig = Text(f"Ảnh gốc (Full rank)", font=VN_FONT, font_size=24, color=WHITE).next_to(frame_right, DOWN)
        ratio_orig = Text("Dung lượng: 100%", font=VN_FONT, font_size=20, color=LIGHT_GRAY).next_to(k_text_orig, DOWN)
        
        txt_right_restored = Text("Ảnh gốc", font=VN_FONT, font_size=24, color=LIGHT_GRAY).move_to(RIGHT * 3.5 + UP * 2.5)

        self.play(
            FadeIn(dim_overlay), 
            FadeIn(frame_right), FadeIn(txt_right_restored),
            FadeIn(img_original), Write(k_text_orig), Write(ratio_orig)
        )
        self.wait(2)

        # --- 5.2. Chuẩn bị bản Zoom (Cắt mảng numpy) ---
        zoom_size = 60 # Cắt vùng 60x60 pixel
        y_start = h // 2 - zoom_size // 2
        x_start = w // 2 - zoom_size // 2

        # Cắt mảng từ ảnh nén (k_target)
        crop_target = target_vis[y_start:y_start+zoom_size, x_start:x_start+zoom_size]
        crop_target_rgb = np.stack((crop_target,)*3, axis=-1)
        zoomed_left = ImageMobject(crop_target_rgb).set_height(4.5).move_to(LEFT * 3.5)

        # Cắt mảng từ ảnh gốc (k_max)
        crop_orig = img_array[y_start:y_start+zoom_size, x_start:x_start+zoom_size]
        crop_orig_rgb = np.stack((crop_orig,)*3, axis=-1)
        zoomed_right = ImageMobject(crop_orig_rgb).set_height(4.5).move_to(RIGHT * 3.5)

        txt_zoom = Text("Phóng to trung tâm (Zoom x5)", font=VN_FONT, font_size=32, color=RED).to_edge(UP)
        
        # --- 5.3. Thực thi hiệu ứng Zoom ---
        self.play(
            FadeOut(k_text_target, ratio_target, k_text_orig, ratio_orig, title_graph),
            Write(txt_zoom)
        )
        
        self.play(
            FadeOut(img_target), FadeOut(img_original),
            FadeIn(zoomed_left), FadeIn(zoomed_right),
            run_time=1.5
        )
        self.wait(4)

        # --- 5.4. Trả 2 hình về kích thước bình thường (Un-zoom) ---
        self.play(
            FadeOut(zoomed_left), FadeOut(zoomed_right), FadeOut(txt_zoom),
            FadeIn(img_target), FadeIn(img_original),
            FadeIn(k_text_target), FadeIn(ratio_target), FadeIn(k_text_orig), FadeIn(ratio_orig)
        )
        self.wait(2)

        # --- 5.5. Trả lại đồ thị bên phải (Giữ nguyên ảnh trái) ---
        # Chỉ FadeOut các đối tượng bên phải và tấm màn đen
        self.play(
            FadeOut(img_original), FadeOut(k_text_orig), FadeOut(ratio_orig), 
            FadeOut(txt_right_restored), FadeOut(frame_right), FadeOut(dim_overlay),
            FadeIn(title_graph) # Hiện lại tiêu đề đồ thị
        )
        self.wait(1)

        # --- 5.6. Hiện Text "Xấp xỉ hạng thấp" đè lên đồ thị ---
        txt_low_rank_1 = Text("Xấp xỉ hạng thấp", font=VN_FONT, font_size=36, color=WHITE)
        txt_low_rank_2 = Text("Low Rank Approx.", font=VN_FONT, font_size=30, color=WHITE).next_to(txt_low_rank_1, DOWN)
        group_txt = VGroup(txt_low_rank_1, txt_low_rank_2).move_to(chart.c2p( (k_max + k_target)/2 , (max_log+min_log)/2 ))
        
        # Nền mờ cho chữ dễ đọc
        bg_for_txt = BackgroundRectangle(group_txt, color=BLACK, fill_opacity=0.7, buff=0.2)

        self.play(FadeIn(bg_for_txt), Write(txt_low_rank_1), Write(txt_low_rank_2))
        self.wait(4)

        # Dọn dẹp
        all_mobs = [m for m in self.mobjects]
        self.play(*[FadeOut(m) for m in all_mobs])
        self.wait(1)














if __name__ == "__main__":
    import os

    # 1. DANH SÁCH CÁC ĐOẠN THEO THỨ TỰ
    SCENES = [
        "Section1_IntroProblem",
        "MatrixDiagonalization",
        "Section23_Theory_And_GeometricSVD",
        "SVDAndDiagonalization", 
        "SVDDecompositionVisual",
        "LowRankTheory",
        "SVDImageCompression"
    ]

    print("BẮT ĐẦU QUÁ TRÌNH TỰ ĐỘNG HÓA MANIM...")
    
    current_file = os.path.basename(__file__)

    # Render tự động từng đoạn
    for scene in SCENES:
        print(f"\n========== ĐANG RENDER: {scene} ==========\n")
        # Lệnh gọi Manim từ hệ thống
        os.system(f"manim -qh {current_file} {scene}")

    # Tạo file danh sách text để FFmpeg đọc
    file_name_without_ext = os.path.splitext(current_file)[0]
    video_dir = f"media/videos/{file_name_without_ext}/1080p60/"
    list_file = "video_list.txt"
    
    print("\n========== ĐANG TẠO DANH SÁCH GHÉP NỐI ==========\n")
    with open(list_file, "w", encoding="utf-8") as f:
        for scene in SCENES:
            path = os.path.join(video_dir, f"{scene}.mp4").replace("\\", "/")
            f.write(f"file '{path}'\n")

    # Gọi FFmpeg để nối video
    output_file = "DO_AN_HOAN_CHINH.mp4"
    print("\n========== ĐANG GHÉP CÁC VIDEO THÀNH 1 FILE DUY NHẤT ==========\n")
    os.system(f"ffmpeg -f concat -safe 0 -i {list_file} -c copy {output_file} -y")
    
    # Dọn dẹp file rác
    if os.path.exists(list_file):
        os.remove(list_file)

    print(f"\n[THÀNH CÔNG] Video của bạn đã sẵn sàng tại thư mục hiện tại: {output_file}")




