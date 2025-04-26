from onderwijsdoelen_nieuw import onderwijsdoelen as od_new
from onderwijsdoelen_oud import onderwijsdoelen as od_old
def main():
    graduation_year = input("When did you finish school? (e.g., 2020): ")

    program_name = input("What program did you follow?: ")

    if 2023 > int(graduation_year):
        od = od_old
    else:
        od = od_new

    with open("rapporten\Competenties.txt", "w") as file:
        file.write(od[program_name])

    

if __name__ == "__main__":
    main()