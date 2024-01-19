from sympy import symbols, solve, Eq

print("GIẢI PHƯƠNG TRÌNH / HỆ PHƯƠNG TRÌNH")
print("by QuangPhuc")
print("________________________________")

print("- Nhập 1 để giải Phương trình")
print("- Nhập 2 để giải Hệ phương trình")
tuy_chon = float(input(">> "))

if tuy_chon ==1:
	x = symbols("x")
	print("Phương trình bậc 2~4 ?")
	bac = float(input(">> "))
	if bac == 2:
		print("Giải phương trình bậc 2 (axᒾ + bx +c =0)")
		a = float(input(">> Nhập a : "))
		b = float(input(">> Nhập b : "))
		c = float(input(">> Nhập c : "))
		
		equation= a*x**2 + b*x + c
		
		print ("Nghiệm của phương trình là : ", solve(equation, x))
		
	elif bac ==3:
		print("Giải phương trình bậc 3(ax³ + bxᒾ + cx + d =0 ")
		a = float(input(">> Nhập a : "))
		b = float(input(">> Nhập b : "))
		c = float(input(">> Nhập c : "))
		d = float(input(">> Nhập d : "))
		
		equation = a*x**3 + b*x**2 + c*x + d
		
		print ("Nghiệm của phương trình là : ", solve(equation, x))
		
	elif bac ==4 :
		print("Giải phương trình bậc 4(ax⁴ + bx³ + cxᒾ + dx + e =0 ")
		a = float(input(">> Nhập a : "))
		b = float(input(">> Nhập b : "))
		c = float(input(">> Nhập c : "))
		d = float(input(">> Nhập d : "))
		e = float(input(">> Nhập e : "))
		
		equation = a*x**4 + b*x**3 + c*x**2 + d*x + e
		
		print ("Nghiệm của phương trình là : ", solve(equation, x))
	else:
		("Không hợp lệ, nhập lại !")
		
elif tuy_chon==2:
	print("Hệ phương trình bậc nhất 2~4 ẩn ?")
	an = float(input(">>"))
	if an == 2 :
		x, y = symbols('x y')
		print("Hệ phương trình bậc nhất 2 ẩn ")
		print("	| a₁x + b₁y = c₁")
		print("	| a₂x + b₂y = c₂")
		
		a1 = float(input(">> Nhập a₁ : "))
		b1 = float(input(">> Nhập b₁ : "))
		c1 = float(input(">> Nhập c₁ : "))
		a2 = float(input(">> Nhập a₂ : "))
		b2 = float(input(">> Nhập b₂ : "))
		c2 = float(input(">> Nhập c₂ : "))
		
		equa1 = Eq(a1*x + b1*y, c1)
		equa2 = Eq(a2*x + b2*y, c2)
	
		solution = solve((equa1, equa2), (x,y))
		
		print("Nghiệm của hệ phương trình là:", solution)
	elif an==3:
		x, y,z = symbols('x y z')
		print("Hệ phương trình bậc nhất 3 ẩn ")
		print("	| a₁x + b₁y + c₁z = d₁")
		print("	| a₂x + b₂y + c₂z = d₂")
		print("	| a₃x + b₃y + c₃z = d₃")
		
		a1 = float(input(">> Nhập a₁ : "))
		b1 = float(input(">> Nhập b₁ : "))
		c1 = float(input(">> Nhập c₁ : "))
		d1 = float(input(">> Nhập d₁ : "))
		a2 = float(input(">> Nhập a₂:  "))
		b2 = float(input(">> Nhập b₂ : "))
		c2 = float(input(">> Nhập c₂ : "))
		d2 = float(input(">> Nhập d₂ : "))
		a3 = float(input(">> Nhập a₃ : "))
		b3 = float(input(">> Nhập b₃ : "))
		c3 = float(input(">> Nhập c₃ : "))
		d3 = float(input(">> Nhập d₃ : "))
		
		equa1 = Eq(a1*x + b1*y + c1*z, d1)
		equa2 = Eq(a2*x + b2*y + c2*z, d2)
		equa3 = Eq(a3*x + b3*y + c3*z, d3)
	
		solution = solve((equa1, equa2, equa3), (x,y,z))
		print("Nghiệm của hệ phương trình là:", solution)

	elif an==4:
		x, y, z, t = symbols('x y z t')
		print("Hệ phương trình bậc nhất 3 ẩn ")
		print("	| a₁x + b₁y + c₁z + d₁t = e₁")
		print("	| a₂x + b₂y + c₂z + d₂t = e₂")
		print("	| a₃x + b₃y + c₃z + d₃t = e₃")
		print("	| a₄x + b₄y + c₄z + d₄t = e₄")
		
		a1 = float(input(">> Nhập a₁ : "))
		b1 = float(input(">> Nhập b₁ : "))
		c1 = float(input(">> Nhập c₁ : "))
		d1 = float(input(">> Nhập d₁ : "))
		e1 = float(input(">> Nhập e₁ : "))
		a2 = float(input(">> Nhập a₂:  "))
		b2 = float(input(">> Nhập b₂ : "))
		c2 = float(input(">> Nhập c₂ : "))
		d2 = float(input(">> Nhập d₂ : "))
		e2 = float(input(">> Nhập e₂ : "))
		a3 = float(input(">> Nhập a₃ : "))
		b3 = float(input(">> Nhập b₃ : "))
		c3 = float(input(">> Nhập c₃ : "))
		d3 = float(input(">> Nhập d₃ : "))
		e3 = float(input(">> Nhập e₃ : "))
		a4 = float(input(">> Nhập a₄ : "))
		b4 = float(input(">> Nhập b₄ : "))
		c4 = float(input(">> Nhập c₄ : "))
		d4 = float(input(">> Nhập d₄ : "))
		e4 = float(input(">> Nhập e₄ : "))
		
		equa1 = Eq(a1*x + b1*y + c1*z + d1*t, e1)
		equa2 = Eq(a2*x + b2*y + c2*z + d2*t, e2)
		equa3 = Eq(a3*x + b3*y + c3*z + d3*t, e3)
		equa4 = Eq(a4*x + b4*y + c4*z + d4*t, e4)
	
		solution = solve((equa1, equa2, equa3, equa4), (x,y,z,t))
		print("Nghiệm của hệ phương trình là:", solution)
	else:
		print("Không hợp lệ, nhập lại !")
else :
	print("Sai cú pháp, nhập lại !")
	
# Coder : Quang Phuc

#Fb : https://www.facebook.com/quangphuc3118?mibextid=ZbWKwL
#github : quangphuc3118
