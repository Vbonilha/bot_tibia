#def check_target():
  # try:
   #     target = pg.locateOnScreen('imgs/red_target.PNG', confidence=0.7, region=region_battle)
    #    if target != None:
    #        print('Esperando o monstro morrer')
    #    else:
    #        print('Procurando outro monstro.')
      #  return target
  #  except pg.ImageNotFoundException:
     #   return None
    

# while pg.locateOnScreen('imgs/red_target.PNG', confidence=0.7, region=region_battle) != None:
         #       print('Esperando o monstro morrer')
         #   print('Procurnado outro monstro.')


import pyautogui as pg

pg.screenshot('Teste.png')