answer = ""
def guess(secretWord):
    # counter = 0
    global answer
    i = 0
    while i != len(secretWord):
        # if(counter == 5):
        #     print("\nKesempatan Habis")
        #     break
        userInput = input(f"Masukan Huruf {i + 1} : ")
        # if(userInput):
        #     counter +=1
        if(userInput.strip() != ""):
              if(userInput.isnumeric()):
                  print("Tidak Boleh Angka")
              else:
                  if(len(userInput) == 1):
                    if(userInput == secretWord[i]):
                        print(f"Huruf {i + 1} Anda Benar")
                        i+=1
                        answer += userInput
                    else:
                        if(userInput.lower() != secretWord[i].lower()):
                            print("Jawaban Salah !")
                        elif(userInput < secretWord[i]):
                            print("Huruf Kecil!")
                        elif(userInput > secretWord[i]):
                            print("Huruf Kapital!")
                        # elif(userInput != secretWord[i]):
                        #     print(f"Huruf {i+1} Salah")
                  else:
                      print("Tidak boleh lebih dari 1 Huruf")           
        else:
            print("Jawaban tidak boleh kosong!")
    print(f"Jawaban anda benar ({answer})")
guess("Duren")
                

