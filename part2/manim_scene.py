from manim import *

VN_FONT = "Arial"
C_MAIN = BLUE_C      
C_LAMBDA = YELLOW_C  
C_VECTOR = GREEN_C   
C_SVD = ORANGE       
C_U = TEAL_C
C_SIGMA = GOLD_C
C_V = PURPLE_C

TITLE_SIZE = 32           
SUBTITLE_SIZE = 26        
FORMULA_MAIN_SIZE = 56    

BODY_TEXT_SIZE = 24       
BODY_MATH_SIZE = 36       

NOTE_TEXT_SIZE = 20      
NOTE_MATH_SIZE = 28      

class IntroProblem(Scene):
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

class Theory_And_GeometricSVD(Scene):
    def construct(self):
        self.show_theory()
        self.show_geometry()

    def show_theory(self):
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
        title = Text("3. Ý nghĩa hình học của SVD", font=VN_FONT, font_size=TITLE_SIZE, color=C_SVD).to_corner(UL)
        self.play(FadeIn(title))

        svd_eq = MathTex("A", "=", "U", "\\Sigma", "V^T", font_size=48).to_corner(UR)
        svd_eq[0].set_color(C_MAIN)
        svd_eq[2].set_color(C_U)
        svd_eq[3].set_color(C_SIGMA)
        svd_eq[4].set_color(C_V)
        self.play(Write(svd_eq))

        geo_center = LEFT * 3.5 + DOWN * 0.5
        
        plane = NumberPlane(
            x_range=[-5, 5], y_range=[-5, 5], 
            x_length=6.5, y_length=6.5, 
            background_line_style={"stroke_opacity": 0.3}
        ).move_to(geo_center)

        origin_pt = plane.get_origin()

        circle = Circle(radius=1.5, color=YELLOW).set_fill(YELLOW, opacity=0.3).move_to(origin_pt)
        
        vec_i = Arrow(start=origin_pt, end=plane.c2p(1.5, 0), buff=0, color=GREEN_C, stroke_width=6, max_tip_length_to_length_ratio=0.15)
        vec_j = Arrow(start=origin_pt, end=plane.c2p(0, 1.5), buff=0, color=RED_C, stroke_width=6, max_tip_length_to_length_ratio=0.15)
        
        center_dot = Dot(origin_pt, radius=0.06, color=WHITE)
        geometry_group = VGroup(circle, vec_i, vec_j)

        self.play(FadeIn(plane))
        self.play(Create(circle), GrowArrow(vec_i), GrowArrow(vec_j), FadeIn(center_dot))

        text_center = RIGHT * 3.5 + DOWN * 0.5

        status_label = VGroup(
            Text("Không gian đầu vào", font=VN_FONT, font_size=BODY_TEXT_SIZE),
            Text("(Đường tròn đơn vị)", font=VN_FONT, font_size=NOTE_TEXT_SIZE, color=LIGHT_GREY)
        ).arrange(DOWN, buff=0.2).move_to(text_center)

        self.play(Write(status_label))
        self.wait(1.5)

        lbl_vt = VGroup(
            Text("Tác động của:", font=VN_FONT, font_size=NOTE_TEXT_SIZE, color=LIGHT_GREY),
            MathTex("V^T", font_size=72, color=C_V), 
            Text("Xoay không gian", font=VN_FONT, font_size=BODY_TEXT_SIZE, color=WHITE),
            Text("(Phép Quay)", font=VN_FONT, font_size=NOTE_TEXT_SIZE, color=LIGHT_GREY)
        ).arrange(DOWN, buff=0.3).move_to(text_center)
        
        angle_vt = -PI / 4 
        matrix_vt = [[np.cos(angle_vt), -np.sin(angle_vt)], [np.sin(angle_vt), np.cos(angle_vt)]]
        
        self.play(
            ReplacementTransform(status_label, lbl_vt),
            Indicate(svd_eq[4], color=C_V, scale_factor=1.5)
        )
        self.play(geometry_group.animate.apply_matrix(matrix_vt, about_point=origin_pt), run_time=2)
        self.wait(1)

        lbl_sigma = VGroup(
            Text("Tác động của:", font=VN_FONT, font_size=NOTE_TEXT_SIZE, color=LIGHT_GREY),
            MathTex("\\Sigma", font_size=72, color=C_SIGMA),
            Text("Kéo giãn trục chính", font=VN_FONT, font_size=BODY_TEXT_SIZE, color=WHITE),
            Text("(Đường tròn \u2192 Ellipse)", font=VN_FONT, font_size=NOTE_TEXT_SIZE, color=LIGHT_GREY)
        ).arrange(DOWN, buff=0.3).move_to(text_center)

        matrix_sigma = [[2.2, 0], [0, 1.2]] 
        
        self.play(
            ReplacementTransform(lbl_vt, lbl_sigma),
            Indicate(svd_eq[3], color=C_SIGMA, scale_factor=1.5)
        )
        self.play(geometry_group.animate.apply_matrix(matrix_sigma, about_point=origin_pt), run_time=2.5)
        self.wait(1)

        lbl_u = VGroup(
            Text("Tác động của:", font=VN_FONT, font_size=NOTE_TEXT_SIZE, color=LIGHT_GREY),
            MathTex("U", font_size=72, color=C_U),
            Text("Xoay đến vị trí đích", font=VN_FONT, font_size=BODY_TEXT_SIZE, color=WHITE),
            Text("(Phép Quay)", font=VN_FONT, font_size=NOTE_TEXT_SIZE, color=LIGHT_GREY)
        ).arrange(DOWN, buff=0.3).move_to(text_center)

        angle_u = PI / 6 
        matrix_u = [[np.cos(angle_u), -np.sin(angle_u)], [np.sin(angle_u), np.cos(angle_u)]]
        
        self.play(
            ReplacementTransform(lbl_sigma, lbl_u),
            Indicate(svd_eq[2], color=C_U, scale_factor=1.5)
        )
        self.play(geometry_group.animate.apply_matrix(matrix_u, about_point=origin_pt), run_time=2)
        self.wait(2)

        self.play(FadeOut(VGroup(title, svd_eq, plane, geometry_group, center_dot, lbl_u)))

class MatrixDiagonalization(Scene):
    def construct(self):
        main_title = Text("4. Bài toán chéo hóa ma trận", font=VN_FONT, font_size=TITLE_SIZE, color=C_SVD).to_corner(UL)
        self.play(FadeIn(main_title))

        res_lambdas = self.step1_find_eigenvalues()
        res_u1 = self.step2_find_eigenvector(
            step_name="Tìm vector riêng cho",
            lam_val="2",
            mat_before="\\begin{pmatrix} 1-2 & 2 \\\\ -1 & 4-2 \\end{pmatrix}",
            transform_op="d_2 - d_1", # THÊM PHÉP BIẾN ĐỔI
            mat_after="\\begin{pmatrix} -1 & 2 \\\\ 0 & 0 \\end{pmatrix}",
            eq_str="-x_1 + 2x_2 = 0",
            vec_res="2 \\\\ 1",
            u_subscript="1", # THÊM CHỈ SỐ VECTOR
            ref_pos_shift=ORIGIN,
            anchor=res_lambdas
        )
        res_u2 = self.step2_find_eigenvector(
            step_name="Tìm vector riêng cho",
            lam_val="3",
            mat_before="\\begin{pmatrix} 1-3 & 2 \\\\ -1 & 4-3 \\end{pmatrix}",
            transform_op="2d_2 - d_1", # THÊM PHÉP BIẾN ĐỔI
            mat_after="\\begin{pmatrix} -2 & 2 \\\\ 0 & 0 \\end{pmatrix}",
            eq_str="-2x_1 + 2x_2 = 0 \\Rightarrow -x_1 + x_2 = 0",
            vec_res="1 \\\\ 1",
            u_subscript="2", # THÊM CHỈ SỐ VECTOR
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

        t_p1 = Text("Đặt", font=VN_FONT, font_size=BODY_TEXT_SIZE)
        t_p2 = MathTex("x_2 = t", font_size=BODY_MATH_SIZE)
        t_p3 = Text("là ẩn tự do", font=VN_FONT, font_size=BODY_TEXT_SIZE)
        t_p4 = MathTex("\\Rightarrow X = t \\begin{pmatrix} " + vec_res + " \\end{pmatrix}", font_size=BODY_MATH_SIZE)
        
        t_step = VGroup(t_p1, t_p2, t_p3, t_p4).arrange(RIGHT, buff=0.15)

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
        # 1. ĐẨY TIÊU ĐỀ LÊN CAO HƠN ĐỂ TIẾT KIỆM KHÔNG GIAN
        step_title = Text("Lập ma trận P và thực hiện chéo hóa", font=VN_FONT, font_size=BODY_TEXT_SIZE, color=BLUE_B).to_corner(UL).shift(DOWN*0.5)
        self.play(FadeIn(step_title))

        # 2. KHỞI TẠO MA TRẬN P
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

        # 3. QUÁ TRÌNH BIẾN ĐỔI CHÉO HÓA (P^-1 A P)
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

        # 4. KẾT LUẬN LÀ MA TRẬN D
        eq4 = MathTex("=", "D", font_size=CALC_FONT_SIZE)
        eq4[1].set_color(C_LAMBDA)
        eq4.next_to(eq3[1], RIGHT, buff=0.3)
        
        self.play(Write(eq4))
        
        final_group = VGroup(eq1, eq2, eq3, eq4)
        final_box = SurroundingRectangle(final_group, color=YELLOW, buff=0.2)
        
        self.play(Create(final_box))
        self.play(Flash(final_box, color=YELLOW))
        self.wait(4)