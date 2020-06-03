
inputuser = str(input("masukkan kalimat: "))
inputuserremove = str(input("masukkan huruf yang ingin dihilangkan: "))

print("dari kalimat", inputuser, ", anda ingin menghilangkan huruf", inputuserremove,".")
print("maka kalimat anda menjadi....")
answer = list(inputuser)
finalanswer = answer.remove(set(inputuserremove)