def max_bending_stress (F,L,b,h):
    sigma_max = (6*F*L)/(b*h**2)
    return sigma_max 
def passes (F,L,b,h,sigma_allow):
    return max_bending_stress (F,L,b,h) <= sigma_allow
