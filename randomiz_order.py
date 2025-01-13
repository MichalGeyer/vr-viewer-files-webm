from pathlib import Path
import shutil
import os
import random

# prompts = os.listdir( 'pairs-user-study-images')
left_root = 'pairs-user-study-webm-ours-left'
right_root = 'pairs-user-study-webm-ours-right/ours_to_the_right'
randomized_save_dir = 'pairs-user-study-webm'
os.makedirs(randomized_save_dir, exist_ok=True)
prompts = [
      "A_glass_door_with_a_sign_reading_'Closed'_in_Hebrew,_showing_reflections_of_the_street",
      "A_minimalist_dining_area_with_modern_furniture_and_decor",
      "A_modern_kitchen_with_cream_cabinetry,_stainless_steel_appliances,_and_a_central_island",
      "A_person_in_white_clothing_is_seen_through_a_window",
    #   "A_person_wearing_sunglasses,_with_a_bright_ceiling_background",
    #   "A_person_wearing_sunglasses_in_a_modern,_minimalistic_room",
      "a_woman_sitting_in_front_of_a_glass_window,_a_cityscape_outside",
      "A_reflection_of_a_woman_on_a_building's_glass_window_with_a_car_parked_nearby",
      "A_reflective_moment_as_a_woman_sits_by_the_window,_listening_to_music_while_gazing_at_the_cityscape_at_dusk",
    #   "A_small_playful_dog_interacting_with_a_ball_on_a_polished_floor.,_cute",
    #   "A_stylishly_dressed_woman_reflected_in_a_shop_window_on_a_sunny_day",
      "A_woman_wearing_a_red_beanie_looking_out_through_a_round_window",
      "Bright_orange_sign_at_a_bus_station_highlighting_a_statistic_about_school_dropouts",
      "Close-up_of_a_tablet_displaying_the_time_16:57_with_a_colorful_light_streak_on_the_screen",
    #   "Close-up_of_someone's_hand_resting_on_a_windowsill,_seen_from_the_outside",
      "Empty_modern_kitchen_interior_seen_through_a_glass_wall",
    #   "Image_of_a_child_reaching_out_towards_a_person,_seen_through_a_glass_panel",
    #   "Man_holding_an_umbrella,_standing_on_a_pier_on_a_rainy_day",
    #   "Nighttime_urban_view_with_building_lights_and_street_reflections",
    #   "Panoramic_cityscape_at_dusk,_showing_urban_buildings_and_lights",
    #   "Rear_view_of_a_parked_car,_with_items_inside_and_reflections_on_the_back_window",
    #   "Red_fire_alarm_panel_mounted_on_a_wall_indoors",
      "Reflection_of_a_dimly_lit_room_with_furniture,_captured_through_a_glass_table",
    #   "Reflection_of_a_man_inside_a_refrigerator_door,_surrounded_by_food_items_and_a_clock_on_the_wall",
      "Side_view_of_a_parked_car,_with_a_reflection_of_a_person_on_the_window",
      "View_of_a_modern_city_skyline_through_a_large_window_with_hanging_decorations",
      "a_classic_office_with_a_desk_and_a_chair",
    #   "a_person_looking_at_buildings_outside_reflected_on_a_glass_window",
      "a_person_looking_out_the_window_at_a_forest,_reflected_on_the_glass",
    #   "a_woman_knocking_outside_knocking_a_glass_window",
      "a_woman_nodding_her_hed_behind_a_glass_door",
    #   "a_woman_sitting_in_front_of_a_glass_window,_a_cityscape_outside_2",
      "TEST-VIDEO-A_lion_standing_near_the_glass,_gazing_outside_the_exhibit",
    #   "a_woman_standing_in_the_balcony_behind_a_glass_door",
    ]

d_order = {}
for viewer in prompts:
    randnum = random.random() if 'TEST' not in viewer else 1
    while randnum == 0.5:
        randnum = random.random()
    if randnum > 0.5:
        d_order[viewer] = 'left'
        src_path = os.path.join(left_root, viewer)
        shutil.move(src_path, randomized_save_dir)
    elif randnum < 0.5:
        d_order[viewer] = 'right'
        src_path = os.path.join(right_root, viewer)
        shutil.move(src_path, randomized_save_dir)


import json
with open('order.json', 'w') as f:
    json.dump(d_order, f)
