
#Imports
import copy
import numpy as np
import cv2
import heapq as hq
import time

# def obstacle_space(canvas):

#     cv2.fillPoly(canvas, pts = [np.array([[460,25], [510,125], [460,225], [460,25]])], color=(255,255,0)) 
#     cv2.fillPoly(canvas, pts = [np.array([[235.04, 87.5], [235.05, 162.5], [300, 200], [364.95, 162.5], [364.95, 87.5], [300, 50], [235.04, 87.5]],np.int32)], color=(255,255,0)) #Hexagon
#     cv2.fillPoly(canvas, pts = [np.array([[100,0],[100,100],[150,100],[150,0],[100,0]])], color =(255,255, 0)) 
#     cv2.fillPoly(canvas, pts = [np.array([[100,150],[100,250],[150,250],[150,150],[100,150]])], color=(255,255,0))

#     return canvas

def MoveUp(curr_loc,canvas):

    location = copy.deepcopy(curr_loc)
    if(location[1]-1 > 0) and (canvas[location[1]-1][location[0]][0]<255):
        location[1] = location[1] - 1 
        return True,tuple(location)
    else:
        return False,tuple(location)

def MoveDown(curr_loc,canvas):

    location = copy.deepcopy(curr_loc)

    if(location[1]+1 < canvas.shape[0]) and (canvas[location[1]+1][location[0]][0]<255):
        location[1] = location[1] + 1 
        return True,tuple(location)
    else:
        return False,tuple(location)

def MoveLeft(curr_loc,canvas):

    location = copy.deepcopy(curr_loc)

    if(location[0]-1 > 0) and (canvas[location[1]][location[0]-1][0]<255):
        location[0] = location[0] - 1 
        return True,tuple(location)
    else:
        return False,tuple(location)
def MoveRight(curr_loc,canvas):
   
    location = copy.deepcopy(curr_loc)

    if(location[0]+1 < canvas.shape[1]) and (canvas[location[1]][location[0]+1][0]<255):
        location[0] = location[0] + 1 
        return True,tuple(location)
    else:
        return False,tuple(location)

def MoveUpRight(curr_loc,canvas):
 
    location = copy.deepcopy(curr_loc)
 
    if(location[1]-1 > 0) and (location[0]+1 <canvas.shape[1]) and (canvas[location[1]-1][location[0]+1][0]<255):
        location[1] = location[1] - 1
        location[0] = location[0] + 1 
        return True,tuple(location)
    else:
        return False,tuple(location)

def MoveDownRight(curr_loc,canvas):

    location = copy.deepcopy(curr_loc)
    if(location[1]+1 < canvas.shape[0]) and (location[0]+1 <canvas.shape[1]) and (canvas[location[1]+1][location[0]+1][0]<255):
        location[1] = location[1] + 1
        location[0] = location[0] + 1 
        return True,tuple(location)
    else:
        return False,tuple(location)

def MoveDownLeft(curr_loc,canvas):

    location = copy.deepcopy(curr_loc)
    if(location[1]+1 < canvas.shape[0]) and (location[0]-1 >0) and (canvas[location[1]+1][location[0]-1][0]<255):
        location[1] = location[1] + 1
        location[0] = location[0] - 1 
        return True,tuple(location)
    else:
        return False,tuple(location)

def MoveUpLeft(curr_loc,canvas):

    location = copy.deepcopy(curr_loc)
    if(location[1]-1 > 0) and (location[0]-1 >0) and (canvas[location[1]-1][location[0]-1][0]<255):
        location[1] = location[1] - 1
        location[0] = location[0] - 1 
        return True,tuple(location)
    else:
        return False,tuple(location)

def Backtracking(start_point, goal_point, closed_list, canvas):
    out = cv2.VideoWriter('Succesful-Test-Case.avi', cv2.VideoWriter_fourcc(*'XVID'), 1000, (canvas.shape[1], canvas.shape[0]))
    path_stack = []
    for key in closed_list.keys():
        canvas[key[1]][key[0]] = [255, 255, 255]
        cv2.imshow("Path Exploration", canvas)
        cv2.waitKey(1)
        out.write(canvas)
    parent_curr_loc = closed_list[tuple(goal_point)]
    path_stack.append(goal_point)
    while parent_curr_loc != start_point:
        path_stack.append(parent_curr_loc)
        parent_curr_loc = closed_list[tuple(parent_curr_loc)]
    cv2.circle(canvas, tuple(start_point), 3, (0, 255, 0), -1)
    cv2.circle(canvas, tuple(goal_point), 3, (0, 0, 255), -1)
    path_stack.append(start_point)
    while len(path_stack) > 0:
        path_curr_loc = path_stack.pop()
        canvas[path_curr_loc[1]][path_curr_loc[0]] = [19, 209, 158]
        out.write(canvas)
        cv2.imshow("Path Exploration", canvas)
    out.release() 

canvas = np.ones((250,600,3),dtype="uint8") #Creating a blank canvas
cv2.fillPoly(canvas, pts = [np.array([[460,25], [510,125], [460,225], [460,25]])], color=(255,255,0)) #Triangle
cv2.fillPoly(canvas, pts = [np.array([[235.04, 87.5], [235.05, 162.5], [300, 200], [364.95, 162.5], [364.95, 87.5], [300, 50], [235.04, 87.5]],np.int32)], color=(255,255,0)) #Hexagon
cv2.fillPoly(canvas, pts = [np.array([[100,0],[100,100],[150,100],[150,0],[100,0]])], color =(255,255, 0)) 
cv2.fillPoly(canvas, pts = [np.array([[100,150],[100,250],[150,250],[150,150],[100,150]])], color=(255,255,0))

start_point = []
goal_point = []

def get_point(point_type):
    while True:
        x = input(f"Enter the X Coordinate of {point_type} Point: ")
        y = input(f"Enter the Y Coordinate of {point_type} Point: ")
        if not (0 <= int(x) < canvas.shape[1] and 0 <= int(y) < canvas.shape[0]):
            print("Enter valid coordinates")
        elif canvas[canvas.shape[0] - int(y) - 1][int(x)][0] == 255:
            print(f"The entered {point_type.lower()} curr_loc is in the obstacle space")
        else:
            return [int(x), int(y)]

start_point = get_point("Start")
goal_point = get_point("Goal")

start_point[1] = canvas.shape[0]-1 - start_point[1]
goal_point[1] = canvas.shape[0]-1 - goal_point[1]

###################### Start Dijistra################################
open_list = []
closed_list = {}
Backtracking_flag = False
hq.heapify(open_list)
hq.heappush(open_list,[0,start_point,start_point])
while(len(open_list)>0):
    curr_loc = hq.heappop(open_list)
    closed_list[(curr_loc[2][0],curr_loc[2][1])] = curr_loc[1]
    curr_cost = curr_loc[0]
    if list(curr_loc[2]) == goal_point:
        Backtracking_flag = True
        print("Back Track")
        break
    for action in [(MoveUp, 1), (MoveUpRight, 1.4), (MoveRight, 1), (MoveDownRight, 1.4)]:
        flag, location = action[0](curr_loc[2], canvas)
        if flag and location not in closed_list:
            temp = False
            for i in range(len(open_list)):
                if open_list[i][2] == list(location):
                    temp = True
                    if (curr_cost + action[1]) < open_list[i][0]:
                        open_list[i][0] = curr_cost + action[1]
                        open_list[i][1] = curr_loc[2]
                        hq.heapify(open_list)
                    break
            if not temp:
                hq.heappush(open_list, [curr_cost + action[1], curr_loc[2], list(location)])
                hq.heapify(open_list)
if(Backtracking_flag):
    Backtracking(start_point,goal_point,closed_list,canvas)

else:
    print("Solution Cannot Be Found")

################ End Dijistra#######################
start_time = time.time()
end_time = time.time() 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
print("Code Execution Time: ",end_time-start_time) 
