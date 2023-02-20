# import pandas csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
import os
import sys
import warnings

# read csv file
df = pd.read_csv("data.csv")
# print(df.head())

# seprate level 1 and level 2 data
df1 = df[df['level'] == 1]
df2 = df[df['level'] == 2]

def level1Stats(df1,level):
    # total attemps for level 1
    total_attempts_level1 = df1['attempts'].sum()
    
    # death by death_by_spike for level 1
    death_by_spike_level1 = df1['death_by_spike'].sum()/total_attempts_level1
    
    # death by death_by_explosive for level 1
    death_by_explosive_level1 = df1['death_by_explosive'].sum()/total_attempts_level1
    
    # death by death_by_spear for level 1
    death_by_spear_level1 = df1['death_by_spear'].sum()/total_attempts_level1
    
    # death by death_by_saw for level 1
    death_by_saw_level1 = df1['death_by_saw'].sum()/total_attempts_level1
    
    # death_by_monster
    death_by_monster_level1 = df1['death_by_monster'].sum()/total_attempts_level1
    
    # death_by_crusher
    death_by_crusher_level1 = df1['death_by_crusher'].sum()/total_attempts_level1
    
    # death_by_falling
    death_by_falling_level1 = df1['death_by_falling'].sum()/total_attempts_level1
    
    # create new plot for each level
    plt.figure()
    # give title to the graph
    plt.title('Average number of deaths by each obstacle for level: '+str(level))
    # give x and y labels
    plt.xlabel('Avg death by Obstacles on level: '+str(level))
    # give y label as % of attempts
    plt.ylabel('% of attempts on level: '+str(level))
    # plot bar graph of attempts for each level to average number of deaths by each obstacle
    plt.bar(['spike', 'explosive', 'spear', 'saw', 'monster', 'crusher', 'falling'], [death_by_spike_level1, death_by_explosive_level1, death_by_spear_level1, death_by_saw_level1, death_by_monster_level1, death_by_crusher_level1, death_by_falling_level1])
    # plt.bar(['death_by_spike', 'death_by_explosive', 'death_by_spear', 'death_by_saw', 'death_by_monster', 'death_by_crusher', 'death_by_falling'], [death_by_spike_level1, death_by_explosive_level1, death_by_spear_level1, death_by_saw_level1, death_by_monster_level1, death_by_crusher_level1, death_by_falling_level1])
    
    # save the plot
    plt.savefig('level'+str(level)+'graph1_stats.png')

    return

# graph 1 stats - average number of deaths by each obstacle for each level
level1Stats(df1,1)
level1Stats(df2,2)

# graph 2 stats - successfull use of powerups for each level

def level1PowerupStats(df1,level):
    # jetpack powerup used
    jetpack_powerup_used_level1 = df1['jetpack_used'].sum()

    # jetpack powerup used and success
    jetpack_powerup_used_success_level1 = df1['jetpack_used_cnt_success'].sum()

    # rope powerup used
    rope_powerup_used_level1 = df1['rope_used'].sum()

    # rope powerup used and success
    rope_powerup_used_success_level1 = df1['rope_used_cnt_success'].sum()

    # spring powerup used
    spring_powerup_used_level1 = df1['spring_used'].sum()

    # spring powerup used and success
    spring_powerup_used_success_level1 = df1['spring_used_cnt_success'].sum()

    # total powerups used
    total_powerups_used_level1 = jetpack_powerup_used_level1 + rope_powerup_used_level1 + spring_powerup_used_level1

    # total powerups used and success
    total_powerups_used_success_level1 = jetpack_powerup_used_success_level1 + rope_powerup_used_success_level1 + spring_powerup_used_success_level1


    # create new plot for each level
    plt.figure()
    # give title to the graph
    plt.title('Successfull use of powerups for level: '+str(level))
    # give x and y labels
    plt.xlabel('Powerups used on level: '+str(level))
    # give y label as % of attempts
    plt.ylabel('% of attempts on level: '+str(level))
    # plot bar graph of attempts for each level to successfull use of powerups
    plt.bar(['jetpack', 'rope', 'spring'], [jetpack_powerup_used_level1/jetpack_powerup_used_success_level1, rope_powerup_used_level1/rope_powerup_used_success_level1, spring_powerup_used_success_level1/spring_powerup_used_level1])
    # plt.bar(['jetpack', 'rope', 'spring'], [jetpack_powerup_used_success_level1, rope_powerup_used_success_level1, spring_powerup_used_success_level1])

    # save the plot
    plt.savefig('level'+str(level)+'graph2_stats.png')

    print('jetpack_powerup_used_level1: ',jetpack_powerup_used_level1)
    print('jetpack_powerup_used_success_level1: ',jetpack_powerup_used_success_level1)
    print('rope_powerup_used_level1: ',rope_powerup_used_level1)
    print('rope_powerup_used_success_level1: ',rope_powerup_used_success_level1)
    print('spring_powerup_used_level1: ',spring_powerup_used_level1)
    print('spring_powerup_used_success_level1: ',spring_powerup_used_success_level1)
    print('total_powerups_used_level1: ',total_powerups_used_level1)
    print('total_powerups_used_success_level1: ',total_powerups_used_success_level1)

    # pie chart for total powerups used and success
    labels = 'total_powerups_used_success_level1', 'total_powerups_used_level1'
    sizes = [total_powerups_used_success_level1, total_powerups_used_level1]
    colors = ['gold', 'yellowgreen']
    explode = (0.1, 0)  # explode 1st slice

    # Plot
    plt.figure()
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    
    plt.axis('equal')
    plt.savefig('level'+str(level)+'piechart_stats.png')

    return

level1PowerupStats(df1,1)
level1PowerupStats(df2,2)


# graph 3 stats - average time spent on each platofrm for each level

def level1PlatformStats(df1,level):
    # avg time to complete the level
    avg_time_to_complete_level1 = df1['time _to_complete_level'].sum()/df1['time _to_complete_level'].count()
    print('avg_time_to_complete_level1: ',avg_time_to_complete_level1)
    # avg time spent on red platform when safe
    avg_time_spent_on_red_platform_when_safe_level1 = df1['red_safe_standing_time'].sum()/df1['red_safe_standing_time'].count()
    print('avg_time_spent_on_red_platform_when_safe_level1: ',avg_time_spent_on_red_platform_when_safe_level1)

    # avg time spent on red platform when not safe
    avg_time_spent_on_red_platform_when_not_safe_level1 = df1['red_unsafe_standing_time'].sum()/df1['red_unsafe_standing_time'].count()
    print('avg_time_spent_on_red_platform_when_not_safe_level1: ',avg_time_spent_on_red_platform_when_not_safe_level1)

    # avg time spent on blue platform when safe
    avg_time_spent_on_blue_platform_when_safe_level1 = df1['blue_safe_standing_time'].sum()/df1['blue_safe_standing_time'].count()
    print('avg_time_spent_on_blue_platform_when_safe_level1: ',avg_time_spent_on_blue_platform_when_safe_level1)

    # avg time spent on blue platform when not safe
    avg_time_spent_on_blue_platform_when_not_safe_level1 = df1['blue_unsafe_standing_time'].sum()/df1['blue_unsafe_standing_time'].count()
    print('avg_time_spent_on_blue_platform_when_not_safe_level1: ',avg_time_spent_on_blue_platform_when_not_safe_level1)

    # total avg time spent on platform when safe
    total_avg_time_spent_on_platform_when_safe_level1 = (avg_time_spent_on_red_platform_when_safe_level1 + avg_time_spent_on_blue_platform_when_safe_level1)/2

    # total avg time spent on platform when not safe
    total_avg_time_spent_on_platform_when_not_safe_level1 = (avg_time_spent_on_red_platform_when_not_safe_level1 + avg_time_spent_on_blue_platform_when_not_safe_level1)/2

    # create new plot for each level
    plt.figure()
    # give title to the graph
    plt.title('Average time spent on each platform for level: '+str(level))
    # give x and y labels
    plt.xlabel('Platform for level: '+str(level))
    # give y label as % of attempts
    plt.ylabel('Average time spent on each platform for level: '+str(level))
    # plot bar graph of attempts for each level to successfull use of powerups
    
    # plot avg time to complete the level on y axis
    # plt.bar(['avg_time_to_complete_level1'], [avg_time_to_complete_level1])

    # plot avg time spent on each platform for each level on x axis
    plt.bar(['green_safe', 'green_unsafe', 'blue_safe', 'blue_unsafe'], [avg_time_spent_on_red_platform_when_safe_level1, avg_time_spent_on_red_platform_when_not_safe_level1, avg_time_spent_on_blue_platform_when_safe_level1, avg_time_spent_on_blue_platform_when_not_safe_level1])

    # plt.bar(['green_safe', 'green_unsafe', 'blue_safe', 'blue_unsafe'], [avg_time_spent_on_red_platform_when_safe_level1, avg_time_spent_on_red_platform_when_not_safe_level1, avg_time_spent_on_blue_platform_when_safe_level1, avg_time_spent_on_blue_platform_when_not_safe_level1])
    # plt.bar(['jetpack', 'rope', 'spring'], [jetpack_powerup_used_success_level1, rope_powerup_used_success_level1, spring_powerup_used_success_level1])

    # save the plot
    plt.savefig('level'+str(level)+'graph3_stats.png')

    return


level1PlatformStats(df1,1)
level1PlatformStats(df2,2)

# graph 4 stats - average number of attempts left at the end of level for each level

def level1AttemptsStats(df):
    # avg number of attempts left at the end of level for level 1 from the dataframe
    # seprate level 1 and level 2 data
    df1 = df[df['level'] == 1]
    df2 = df[df['level'] == 2]
    print(df1['number_of_attempts_left'].count())
    print(df2['number_of_attempts_left'].count())
    print(df2.head(10))
    # avg number of attempts left at the end of level for level 1
    avg_attempts_left_level1 = df1['number_of_attempts_left'].sum()/df1['number_of_attempts_left'].count()
    print('avg_attempts_left_level1: ',avg_attempts_left_level1)

    # avg number of attempts left at the end of level for level 2
    avg_attempts_left_level2 = df2['number_of_attempts_left'].sum()/df2['number_of_attempts_left'].count()
    print('avg_attempts_left_level2: ',avg_attempts_left_level2)
    print(df2['number_of_attempts_left'].count())

    # create new plot for each level
    plt.figure()
    # give title to the graph
    plt.title('Average number of attempts left at the end of level for level: ALL')
    # give x and y labels
    plt.xlabel('Level: ALL')
    # give y label as % of attempts
    plt.ylabel('Average number of attempts left at the end of level for level: ALL')
    # plot bar graph of attempts for each level to successfull use of powerups
    plt.bar(['level1', 'level2'], [avg_attempts_left_level1, avg_attempts_left_level2])
    # save the plot
    plt.savefig('level_all'+'graph4_stats.png')

    return

level1AttemptsStats(df)

# graph 5 stats - scatter plot for where the player died in the level

def level1DeathLocationStats(df1,level):
    # get location of death for player in a string format from the dataframe
    locations = df1['death_location_of_player'].tolist()
    print(locations)
    # get the x and y coordinates of the death location
    x = []
    y = []
    for location in locations:
        temp = location.split(',')
        for i in range(len(temp)):
            x.append(temp[i].split(':')[0])
            y.append(temp[i].split(':')[1])
    print(x)
    print(y)
level1DeathLocationStats(df1,1)