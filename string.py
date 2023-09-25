#string conversion
#implicit
name="preetham"
print(name)
print(type(name))

#explicit
name=str("preetham")
print(name)
print(type(name))

#data type annoation
name:str="preetham"
print(name)
print(type(name))

#octal
a=str(0o5314544)
print(a)
print(type(a))

##binary
a=int(0b11001)
print(a)
print(type(a))

#hexadecmial
a=int(0xbaf)
print(a)
print(type(a))

#boolean
a = str(True)
print(a)
print(type(a))
#b00lean conversion
a = bool("abc")
print(a)
print(type(a))
#hexa conversion
a = hex("abc")
print(a)
print(type(a))
#octal conversion
a = oct("abc")
print(a)
print(type(a))
#binary conversion
a = bin("abc")
print(a)
print(type(a))
