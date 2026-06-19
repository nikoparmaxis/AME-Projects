import beam_utils as bu

# Case A 
F = 1000
L = 2.0 
b = 0.05
h = 0.10
sigma_allow = 30.0e6

sigma_max = bu.max_bending_stress(F,L,b,h)
passes = bu.passes(F,L,b,h,sigma_allow)

print(sigma_max)
if passes:
    print('pass')
else:
    print('fail')
    print(f'exceeds by: {sigma_max-sigma_allow} Pa') 


# Case B 
F = 2000
L = 2.0 
b = 0.05
h = 0.10
sigma_allow = 30.0e6

sigma_max = bu.max_bending_stress(F,L,b,h)
passes = bu.passes(F,L,b,h,sigma_allow)

print(sigma_max)
if passes:
    print('pass')
else:
    print('fail')
    print(f'exceeds by: {sigma_max-sigma_allow} Pa') 
