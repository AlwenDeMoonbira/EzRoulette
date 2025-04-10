import tkinter as tk

import tkinter

from tkinter import messagebox
import random

bullet=[0,0,0,0,0,0]
item_list=['cigarette','magnifier','handcuffs','knife']
player_heal=int(3)
dm_heal=int(3)
true_bullet=0
false_bullet=0
item_own=['','','','','','','','']
item_used=[1,1,1,1,1,1,1,1]
loaded_Bu=0
KnifeMark=0
HandMark=0
def trigger_pulled():           #子弹上膛，初始化
    global true_bullet,false_bullet,player_heal,dm_heal,item_own,loaded_Bu,bullet_area,item_used
    true_bullet=0
    false_bullet=0
    loaded_Bu=0
    random_number = random.randint(0, 1)
    item_used=[1,1,1,1,1,1,1,1]
    #print(random_number)
    tem=0
    loaded_Bu=0
    for i in bullet:
        bullet[tem]=random.randint(0, 1)
        if bullet[tem]==1:
            true_bullet+=1
        else:
            false_bullet+=1
        tem+=1
    
        #print(bullet[tem-1])
    print(bullet,true_bullet,false_bullet)
    tem=0    
    for i in item_own:
        item_own[tem]=random.randint(0, 3)
        print(item_own[tem])
        tem+=1
    print(item_own)

    player_heal,dm_heal=3,3
    cheakout()
    print('EveryThing has reset!')
    print('Try2Win')
    tk.messagebox.showinfo("The shotgun has been reloaded","EveryThing has reset \n Try2Win")
    #print(tk.messagebox.asktrycancel(title='Hi', message='hahahaha'))
    
def cheakout():     #刷新面板和道具栏
    global bullet,true_bullet,false_bullet,player_heal,dm_heal,item_own,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,bullet_area,loaded_Bu
    btn5.config(text=item_list[item_own[4]])
    btn6.config(text=item_list[item_own[5]])
    btn7.config(text=item_list[item_own[6]])
    btn8.config(text=item_list[item_own[7]])
    btn1.config(text=item_list[item_own[0]])
    btn2.config(text=item_list[item_own[1]])
    btn3.config(text=item_list[item_own[2]])
    btn4.config(text=item_list[item_own[3]])
    bullet_area.config(text=' DeclarerHeal:'+str(dm_heal)+' YourHeal:'+str(player_heal)+'\n TrueBullet:'+str(true_bullet)+' FalseBullet:'+str(false_bullet))
# ===== 按钮回调函数 =====
def shoot_dealer():
    global bullet,true_bullet,false_bullet,player_heal,dm_heal,item_own,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,bullet_area,loaded_Bu,HandMark,KnifeMark
    print("你向庄家射击！",loaded_Bu)
    if bullet[loaded_Bu]==1:
        tk.messagebox.showinfo("Block!",'your attack worked')
        dm_heal=dm_heal-1
        if KnifeMark==1:
            dm_heal=dm_heal-1
            tk.messagebox.showinfo("Knife",'Because of the effect of knife,\n there is one more damage')
            KnifeMark=0
        loaded_Bu=loaded_Bu+1
        true_bullet=true_bullet-1
        cheakout()
        finish()
        if HandMark == 0:
            AImove()
        else:
            tk.messagebox.showinfo("HandCuff","The declarer still needs one turn to break free from the handcuffs")
            HandMark=0
    else:
        tk.messagebox.showinfo("Miss!","pity")
        KnifeMark=0
        loaded_Bu=loaded_Bu+1
        false_bullet=false_bullet-1
        cheakout()
        finish()
        if HandMark == 0:
            AImove()
        else:
            tk.messagebox.showinfo("HandCuff","The declarer still needs one turn to break free from the handcuffs")
            HandMark=0
def shoot_self():
    global bullet,true_bullet,false_bullet,player_heal,dm_heal,item_own,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,bullet_area,loaded_Bu,HandMark,KnifeMark
    print("你向自己射击！",loaded_Bu)
    if bullet[loaded_Bu]==1:
        tk.messagebox.showinfo("Oach!",'You serious? \n you guys shot yourself!??')
        player_heal=player_heal-1
        if KnifeMark==1:
            player_heal=player_heal-1
            tk.messagebox.showinfo("Knife",'Because of the effect of knife,\n there is one more damage')
            KnifeMark=0
        loaded_Bu=loaded_Bu+1
        true_bullet=true_bullet-1
        cheakout()
        finish()
        if HandMark == 0:
            AImove()
        else:
            tk.messagebox.showinfo("HandCuff","The declarer still needs one turn to break free from the handcuffs")
            HandMark=0
    else:
        tk.messagebox.showinfo("GoodJob","It's the ward to a brave guy \n you can move again now")
        loaded_Bu=loaded_Bu+1
        KnifeMark=0
        false_bullet=false_bullet-1
        cheakout()
        finish()
        #AImove()
def end_turn():
    global bullet,true_bullet,false_bullet,player_heal,dm_heal,item_own,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,bullet_area,loaded_Bu
    print("this button's fuction is still in building")



def use_item(index):
    global bullet,true_bullet,false_bullet,player_heal,dm_heal,item_own,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,bullet_area,loaded_Bu
    print(f"使用道具 {index + 1}")

def declarer_move():
    global bullet,true_bullet,false_bullet,player_heal,dm_heal,item_own,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,bullet_area,loaded_Bu
    print(f"使用道具 {index + 1}")
def finish():
    global bullet,true_bullet,false_bullet,player_heal,dm_heal,item_own,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,bullet_area,loaded_Bu
    if player_heal==0:
        tk.messagebox.showinfo("LOSE","Your heal ran out, you lose!")
        root.quit()
        root.destroy()
    if dm_heal==0:
        tk.messagebox.showinfo("Win","Declarer has use out his heal,You win!")
        root.quit()
        root.destroy()
    if loaded_Bu==6:
        tk.messagebox.showinfo("Bullet has ran out","We stil need a rank,dosen't us?")
        tem1=player_heal
        tem2=dm_heal
        trigger_pulled()
        player_heal=tem1
        dm_heal=tem2
        cheakout()
#============================================分割线==以下为ai行为逻辑==============================================================================================================================
def AImove():
    successmark=0
    global true_bullet,false_bullet,player_heal,dm_heal,item_own,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,bullet_area,loaded_Bu
    print(loaded_Bu,'——————————————————————————')
    if true_bullet>=false_bullet:
        print('declarer shot to you')
        if bullet[loaded_Bu]==1:
            player_heal=player_heal-1
            loaded_Bu=loaded_Bu+1
            tk.messagebox.showinfo("Oach","You got shot!")
            true_bullet=true_bullet-1
        else:
            loaded_Bu=loaded_Bu+1
            tk.messagebox.showinfo("Well","Nothing happend")
    else:
        print('declarer shot to himself')
        if bullet[loaded_Bu]==1:
            dm_heal=dm_heal-1
            tk.messagebox.showinfo("haha","Declarer shot himself \n He deserved it,didn't he?")
            loaded_Bu=loaded_Bu+1
            true_bullet=true_bullet-1
        else:
            tk.messagebox.showinfo("Nothing happend")
            loaded_Bu=loaded_Bu+1
            successmark=1
    cheakout()
    finish()
    if successmark==1:
        tk.messagebox.showinfo("Because his brave, he can move again")
        finish()
        AImove()
        
        
#============================================分割线================================================================================================================================
def useit(a):
    global true_bullet,false_bullet,player_heal,dm_heal,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,bullet_area,loaded_bu,loaded_Bu,HandMark,KnifeMark
    if item_list[item_own[a]] == 'cigarette' and item_used[a] ==1:
        player_heal=player_heal+1
        tk.messagebox.showinfo("You used the cigarette","Your heal plus one")

    elif item_list[item_own[a]] == 'magnifier' and item_used[a] ==1:
        if bullet[loaded_Bu]==1:
            tk.messagebox.showinfo("You used the magnifier","The next bullet is TRUE")
        else:
            tk.messagebox.showinfo("You used the magnifier","The next bullet is False")
    elif item_list[item_own[a]] == 'handcuffs' and item_used[a] ==1:
        tk.messagebox.showinfo("You used the handcuff","The next trun of declarer will be skipped")
        HandMark=1
    elif item_list[item_own[a]] == 'knife' and item_used[a] ==1:
        tk.messagebox.showinfo("You used the handcuff","The next damage of bullet will become to 2")
        KnifeMark=1
    else:
        usedout()
    item_used[a]=0
def usedout():
    tk.messagebox.showinfo("There is nothing left","So UR trying to use a ball of air?")
    




def use_item_1():
    global bullet,true_bullet,false_bullet,player_heal,dm_heal,item_own,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,bullet_area,loaded_bu,loaded_Bu
    print("使用道具 1")
    #if 
def use_item_2():
    global bullet,true_bullet,false_bullet,player_heal,dm_heal,item_own,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,bullet_area,loaded_bu,loaded_Bu
    print("使用道具 2")

def use_item_3():
    global bullet,true_bullet,false_bullet,player_heal,dm_heal,item_own,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,bullet_area,loaded_bu,loaded_Bu
    print("使用道具 3")

def use_item_4():
    global bullet,true_bullet,false_bullet,player_heal,dm_heal,item_own,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,bullet_area,loaded_bu,loaded_Bu
    print("使用道具 4")

def use_item_5():
    global bullet,true_bullet,false_bullet,player_heal,dm_heal,item_own,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,bullet_area,loaded_bu,loaded_Bu
    print("使用道具 5")
    useit(4)
    btn5.config(text="Used")
    cheakout()
def use_item_6():
    global bullet,true_bullet,false_bullet,player_heal,dm_heal,item_own,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,bullet_area,loaded_bu,loaded_Bu
    print("使用道具 6")
    useit(5)
    btn6.config(text="Used")
    cheakout()
def use_item_7():
    global bullet,true_bullet,false_bullet,player_heal,dm_heal,item_own,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,bullet_area,loaded_bu,loaded_Bu
    print("使用道具 7")
    useit(6)
    btn7.config(text="Used")
    cheakout()
def use_item_8():
    global bullet,true_bullet,false_bullet,player_heal,dm_heal,item_own,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,bullet_area,loaded_bu,loaded_Bu
    print("使用道具 8")
    useit(7)
    btn8.config(text="Used")
    cheakout()
# 创建主窗口
root = tk.Tk()
root.title("RouletteG")
root.geometry("800x600")  # 可以根据需要调整窗口大小

# 整体使用一个水平的框架：左侧功能区 + 右侧按钮区
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# 左侧区域
left_frame = tk.Frame(main_frame, width=500)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# 右侧区域
right_frame = tk.Frame(main_frame, width=300)
right_frame.pack(side=tk.RIGHT, fill=tk.Y)

# ===== 左侧上方道具区 =====
top_items_frame = tk.Frame(left_frame)
top_items_frame.pack(side=tk.TOP, pady=20)

top_item_buttons = []
btn1 = tk.Button(top_items_frame, text="You", width=8, height=4, command=use_item_1)
btn1.pack(side=tk.LEFT, padx=5)

btn2 = tk.Button(top_items_frame, text="Need", width=8, height=4, command=use_item_2)
btn2.pack(side=tk.LEFT, padx=5)

btn3 = tk.Button(top_items_frame, text="To", width=8, height=4, command=use_item_3)
btn3.pack(side=tk.LEFT, padx=5)

btn4 = tk.Button(top_items_frame, text="Win", width=8, height=4, command=use_item_4)
btn4.pack(side=tk.LEFT, padx=5)

# ===== 中间子弹区（预留设计）=====
bullet_area = tk.Label(left_frame, text="Welcome To ROULETTEGAME", bg="gray", width=40, height=10)
bullet_area.pack(pady=30)

# ===== 左侧下方道具区 =====
bottom_items_frame = tk.Frame(left_frame)
bottom_items_frame.pack(side=tk.BOTTOM, pady=20)

bottom_item_buttons = []
btn5 = tk.Button(bottom_items_frame, text="Instead", width=8, height=4, command=use_item_5)
btn5.pack(side=tk.LEFT, padx=5)

btn6 = tk.Button(bottom_items_frame, text="Of", width=8, height=4, command=use_item_6)
btn6.pack(side=tk.LEFT, padx=5)

btn7 = tk.Button(bottom_items_frame, text="The", width=8, height=4, command=use_item_7)
btn7.pack(side=tk.LEFT, padx=5)

btn8 = tk.Button(bottom_items_frame, text="Death", width=8, height=4, command=use_item_8)
btn8.pack(side=tk.LEFT, padx=5)

# ===== 右侧主要按钮区 =====
# 横向按钮区
right_buttons_frame = tk.Frame(right_frame)
right_buttons_frame.pack(pady=200)

btn_shoot_dealer = tk.Button(right_buttons_frame, text="Fire to Declarer", width=12, height=2,
                              bg="red", fg="white", command=shoot_dealer)
btn_shoot_dealer.pack(side=tk.LEFT, padx=5)

btn_end_turn = tk.Button(right_buttons_frame, text="None", width=12, height=2,
                         bg="gray", fg="white", command=end_turn)
btn_end_turn.pack(side=tk.LEFT, padx=5)

btn_shoot_self = tk.Button(right_buttons_frame, text="Fire to yourself", width=12, height=2,
                            bg="blue", fg="white", command=shoot_self)
btn_shoot_self.pack(side=tk.LEFT, padx=5)

# ===== 扳机按钮 =====
trigger_button = tk.Button(right_frame, text="trigger", width=20, height=3,
                           bg="black", fg="white", command=trigger_pulled)
trigger_button.pack(side=tk.BOTTOM, pady=40)





# 启动主循环
root.mainloop()
