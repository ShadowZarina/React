#include <stdio.h>
#include <string.h>

void addTasks(char tasks[][100], int *length) {
    printf("Enter a new task:");
    scanf("%s", tasks[length]);
    length++;
}

void viewTasks(char tasks[][100], int *length) {
    int i;

    printf("To-Do List:\n");
        
        if (length == 0) {
            printf("No tasks left to do!");
            return;
        } else {
            for (i = 0; i < length; i++) {
                printf("%d. %s\n", i+1, tasks[i]);
            }
        }
}

void deleteTasks(char tasks[][100], int *length) {
    int i, index;

    if (length == 0) {
            printf("No tasks available to delete!");
            return 1;
        } else {
            for (i = 0; i < length; i++) {
                if (i == length - 1) {
                    printf("\n%d. %s", i+1, tasks[i]);
                } else {
                    printf("\n%d. %s, ", i+1, tasks[i]);
                }
            }
        }

    printf("\nEnter the number of the task you want to delete:");
    scanf("%d", &index);

    for (i = index - 1; i < length - 1; i++) {
        strcpy(tasks[i], tasks[i + 1]);
    }

    length--;
}

int main() {
    int choice, i, length = 0;
    char tasks[10][100];

    while (1) {
        printf("----- TO-DO LIST ----- \n");
        printf("1. Add Task\n");
        printf("2. View Tasks\n");
        printf("3. Delete Task\n");
        printf("4. Exit\n");
        printf("Enter a choice:");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                addTasks(tasks, length);
                return;
            case 2:
                viewTasks(tasks, length);
                return;
            case 3:
                deleteTasks(tasks, length);
                return;
            case 4:
                printf("Closing the program.");
                return 0;
            default:
                break;
        }
    }

    return 0;
}
