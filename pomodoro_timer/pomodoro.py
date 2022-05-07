import winsound
import time
import sys



def getToDoList():
    toDoList = []
    print("To stop the list, enter 'DONE'")
    while True:
        todoInput = input("Enter a task you wish to complete: ")
        if todoInput == "DONE":
            break
        else:
            toDoList.append(todoInput)
    return toDoList

def pomoTimer(minutes, list, listNumber):
    print("Your task is: ", end= "")
    print(list[listNumber - 1])
    #time.sleep(minutes * 60) REAL
    time.sleep(10)
    if listNumber % 4 == 0:
        print("Take a 15 - 30 minute break")
    else:
        print("Take a 5 minute break")
    winsound.Beep(500,2000)
    while True:
        doneWithTimer = input("Done with your break? y/n: ")
        if doneWithTimer == "y":
            break
    




def main():
    timerCounts = 0
    print("Welcome to Pomodoro by Grange Co.")
    todoList = getToDoList()
    for i in todoList:
        print("Starting a 25 minute timer, get started on your task")
        timerCounts += 1
        pomoTimer(25, todoList, timerCounts)
    
    print("Great Job today! Come back again soon")
    print("Today you got done with ",end= "")
    for i in todoList:
        print(i,end = ", ")

    



main()