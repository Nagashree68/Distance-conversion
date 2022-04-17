dist = int(input("input the distance travelled:"))
unit = input ("input  type i.e.,K for kilometer M for miles" )
if unit == "K":
    converted = dist/1.609
    print(f"you have covered{converted}miles" )
else:
    converted = dist*1.609
    print(f"you have covered{converted }kms" )


#
dist = int(input("input the distance covered:"))
unit = input ("input type i.e.,K for kilometers M for miles")
if unit == "K":
    converted = dist / 1.609
    print(f"you have covered{converted}miles")
elif unit == "M":
    converted = dist * 1.609
    print(f"you have covered{converted}kms")
else:
    print("wrong input")
