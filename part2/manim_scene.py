from manim import *
import numpy as np

# BẢNG MÀU TỔNG HỢP (Gộp từ cả 2 file)
VN_FONT = "Arial"
C_MAIN = BLUE_C      
C_LAMBDA = YELLOW_C  
C_VECTOR = GREEN_C   
C_SVD = ORANGE       
C_U = TEAL_C
C_SIGMA = GOLD_C
C_V = PURPLE_C

# Thêm màu cho SVD Premium Geometry
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