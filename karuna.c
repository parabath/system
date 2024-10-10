#include <stdio.h>
#include <stdlib.h>

int main() {
int myNum;

printf("\n 1-patient_list\n 2-patient_res\n");

// Ask the user to type a number
printf("Type a number: \n");

// Get and save the number the user types
scanf("%d", &myNum);

// Output the number the user typed
printf("Your number is: %d", myNum);

if(myNum==0){
    printf("\n1-patients_list \n2-patients_res \n3 \n");
    system("karuna.bat");
}
else if (myNum==1){
    printf("\n  patients details with patient number\n");
    system("kindex.bat"); 
}
else if (myNum==2){
    printf("\n patients pix\n");
    system("kindexpix.bat"); 
}
else if (myNum==3){
    printf("\n 3d book\n");
    system("book.bat"); 
}
else if (myNum==4){
    printf("\na-note1 \nb-note2 \nb-note3 \n \nc,d,e...\n");
    system("psv.bat"); 
}
else if (myNum==5){
    printf("\nbee_3d\n");
    system("msc.bat"); 
}
    // Replace "your_batch_file.bat" with the actual path to your batch file
    
    return 0;
}
