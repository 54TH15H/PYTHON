import random
import time

import pyautogui
from PIL import ImageGrab

no_of_submits = 2

main_menu_options_x = [1655, 1649, 1722, 1731, 1763, 1635, 1756, 1659, 1777]
main_menu_options_y = [578, 628, 674, 726, 777, 824, 823, 872, 873]
main_menu_options_colors = [(200, 160, 62), (54, 120, 178), (88, 180, 202), (150, 148, 152), (220, 163, 77), (107, 67, 62), (213, 177, 61), (196, 163, 50), (104, 53, 88)]

chat_experience_options_x = [1596, 1742, 1677, 1582, 1703, 1801, 1582]
chat_experience_options_y = [556, 555, 603, 650, 656, 655, 817]

shipping_policy_options_x = [1578, 1641, 1573, 1713, 1644, 1614]
shipping_policy_options_y = [497, 665, 712, 711, 761, 809]

delivery_areas_options_x = [1629, 1641, 1573, 1713, 1644, 1614]
delivery_areas_options_y = [614, 665, 712, 711, 761, 809]

payment_faq_options_x = [1601, 1601, 1672, 1640, 1641, 1657]
payment_faq_options_y = [501, 552, 602, 670, 741, 787]

payment_methods_options_x = [1569, 1558, 1791, 1551, 1643]
payment_methods_options_y = [763, 809, 810, 861, 858]

bank_transfer_options_x = [1537, 1595, 1611]
bank_transfer_options_y = [811, 812, 860]

help_with_shopping_options_x = [1570, 1732, 1658, 1654, 1638, 1648]
help_with_shopping_options_y = [594, 593, 641, 713, 763, 811]

loyalty_points_options_x = [1617, 1620, 1664, 1637, 1652]
loyalty_points_options_y = [573, 622, 673, 742, 793]

coupons_options_x = [1618, 1635, 1642, 1661, 1631, 1660]
coupons_options_y = [504, 552, 602, 672, 743, 790]

auctions_options_x = [1651, 1630, 1642, 1639, 1625]
auctions_options_y = [665, 716, 762, 809, 861]

manage_order_options_x = [1587, 1612, 1576, 1732, 1627, 1604, 1608, 1585, 1621]
manage_order_options_y = [467, 517, 565, 568, 616, 663, 710, 761, 813]

# VPN countries list
vpn_countries = ["india", "germany", "france", "ireland", "japan", "russia", "singapore"]

urls = ["urlOne", "urlTwo", "urlThree"]
url = urls[random.randint(0, len(urls)-1)]

vpn_not_connected = True

def main():

    print("Waiting for 10 seconds...")
    time.sleep(10)

    # get_coordinates_and_pixels()

    counter = 1

    while counter <= no_of_submits:

        print("{} : Clicking on Top Right Three Dots".format(counter))
        move_click(1883, 78)

        print("{} : Opening New Incognito window".format(counter))
        move_click(1727, 256) # (1788, 200)

        global vpn_not_connected
        if vpn_not_connected:
            print("{} : VPN not yet connected".format(counter))
            handle_vpn()
            vpn_not_connected = False

        print("{} : Opening {}".format(counter, url))
        open_web_page()

        continue_to_site_or_accept_cookies()

        print("{} : Zooming out Incognito window".format(counter))
        zoom_out()

        print("{} : Refreshing Incognito window".format(counter))
        refresh()

        print("{} : Opening chatbot".format(counter))
        open_chatbot()

        print("{} : Waiting for options".format(counter))
        wait_for_options()

        time.sleep(1)

        print("{} : start_selecting_options".format(counter))
        start_selecting_options()

        time.sleep(5)

        recheck()
        print("{} : Closing bot".format(counter))
        time.sleep(1)
        move_click(1848, 301)

        recheck()
        print("{} : End Chat Button".format(counter))
        move_wait_click(1621, 915, (242, 109, 134)) # end_chat()

        recheck()
        print("{} : Clicking like button".format(counter))
        move_click(1645, 779)

        time.sleep(1)

        print("{} : Giving chat experience".format(counter))
        select_option(chat_experience_options_x, chat_experience_options_y)

        time.sleep(1)

        recheck()
        print("{} : Clicking on submit button".format(counter))
        move_wait_click(1628, 930, (139, 16, 119))

        time.sleep(2)

        recheck()
        print("{} : Closing Incognito window".format(counter))
        move_click(1890, 28)

        print("\nBot used {} times successfully.\n".format(counter))

        counter = counter + 1

def end_chat():

    end_chat_clicked = False

    while True:

        if end_chat_clicked:
            break

        recheck()
        pyautogui.moveTo(1848, 301)
        recheck()
        pyautogui.click()

        start_time = time.time()

        print("Waiting for end chat button...")
        while True:
            pyautogui.moveTo(1621, 915, duration=1)
            screenshot = ImageGrab.grab()
            color = screenshot.getpixel((1621, 915))

            if color == (242, 109, 134):
                time.sleep(1)
                pyautogui.moveTo(1621, 915, duration=1)
                time.sleep(1)
                recheck()
                time.sleep(1)
                pyautogui.click()
                end_chat_clicked = True
                break

            if time.time() - start_time > 10:
                recheck()
                break

def open_web_page():

    time.sleep(5)

    # Clicking on Search box
    move_click(372, 79)

    pyautogui.write(url, interval=0.1)

    pyautogui.press("enter")

def move_click(i, j):

    pyautogui.moveTo(i, j, duration=1)

    time.sleep(1)

    pyautogui.click()

def move_wait_click(i, j, target):

    move_wait(i, j, target)

    time.sleep(1)

    pyautogui.click()

def move_wait(i, j, target):

    pyautogui.moveTo(i, j, duration=1)

    print("Waiting until target color {} found".format(target))

    start_time = time.time()

    while True:
        screenshot = ImageGrab.grab()
        pixel_color = screenshot.getpixel((i, j))

        if pixel_color == target:
            break

        print("x:{},y:{},color:{} => ".format(i,j,target), end="")
        time.sleep(1)

        if time.time() - start_time > 10:
            recheck()

    print()

def zoom_out():

    # Clicking on 3 dots to make zoom out
    move_click(1889, 77)

    time.sleep(1)

    # Clicking on zoom out button
    move_click(1730, 511)

    time.sleep(1)

    # Clicking on zoom out button
    pyautogui.click()

    time.sleep(1)

def refresh():

    move_wait(77, 24, (145, 8, 125))

    move_click(114, 83)

    time.sleep(2)


def continue_to_site_or_accept_cookies():

    print("continue_to_site_or_accept_cookies")
    # move cursor to "continue to site" button or "accept cookies" button
    time.sleep(1)
    pyautogui.moveTo(716, 776, duration=1)
    time.sleep(1)

    while True:
        time.sleep(1)
        screenshot = ImageGrab.grab()
        color = screenshot.getpixel((716, 776))

        # Continue to site
        if color == (8, 66, 160):
            time.sleep(1)
            pyautogui.click()
            print("Clicked on 'continue to site'")
            continue

        # Accept cookies
        elif color == (179, 88, 164) or color == (147, 17, 126):
            time.sleep(1)
            pyautogui.click()
            print("Cookies accepted")
            break

        else:
            time.sleep(1)
            print(".",end="")


def get_coordinates_and_pixels():

    i, j = pyautogui.position()
    print(f"Cursor position: ({i}, {j})")

    screenshot = ImageGrab.grab()
    pixel_color = screenshot.getpixel((i, j))

    print(f"Pixel color: {pixel_color}")

    exit(0)

def recheck():

    i, j = pyautogui.position()

    screenshot = ImageGrab.grab()
    color = screenshot.getpixel((1814, 956))

    if color == (147, 17, 126):
        print("Chatbot closed unexpectedly!")
        pyautogui.moveTo(1814, 956, duration=1)
        pyautogui.click()
        print("Reopened chatbot")

    pyautogui.moveTo(i, j, duration=1)
    time.sleep(1)

def start_selecting_options():

    index = random.randint(0, len(main_menu_options_x)-1)

    while True:
        move_click(main_menu_options_x[index], main_menu_options_y[index])

        print("Selected main menu option: {}, {}".format(main_menu_options_x[index],main_menu_options_y[index]))

        time.sleep(1)

        recheck()

        screenshot = ImageGrab.grab()
        color = screenshot.getpixel((main_menu_options_x[index], main_menu_options_y[index]))

        if color == main_menu_options_colors[index]:
            continue

        break

    if index == 1:

        option_selected = select_option(shipping_policy_options_x, shipping_policy_options_y)
        print("Selected shipping policy option: {}".format(option_selected))

        if option_selected == 0:
            option_selected = select_option(delivery_areas_options_x, delivery_areas_options_y)
            print("Selected delivery area option: {}".format(option_selected))

            if option_selected == 0 or option_selected == 1:
                pyautogui.moveTo(1655, 689, duration=1)
                pyautogui.click()
                recheck()

    elif index == 2:
        select_option(manage_order_options_x, manage_order_options_y)
        print("Selected manage order option: {}".format(manage_order_options_x))

    elif index == 3:
        select_option(help_with_shopping_options_x, help_with_shopping_options_y)
        print("Selected help with shopping option: {}".format(help_with_shopping_options_x))

    elif index == 4:
        move_wait(1838, 926, (128, 128, 128))
        time.sleep(1)
        pyautogui.moveTo(1688, 963, duration=1)
        time.sleep(1)
        pyautogui.click()
        print("Clicked on 'Cancel' button'")
        recheck()

    elif index == 5:
        option_selected = select_option(payment_faq_options_x, payment_faq_options_y)
        print("Selected payment faq option: {}".format(option_selected))

        if option_selected == 0:
            option_selected = select_option(payment_methods_options_x, payment_methods_options_y)
            print("Selected payment method option: {}".format(option_selected))

            if option_selected == 0:
                select_option(bank_transfer_options_x, bank_transfer_options_y)
                print("Selected bank transfer option: {}".format(option_selected))

    elif index == 6:
        option_selected = select_option(coupons_options_x, coupons_options_y)
        print("Selected coupons option: {}".format(option_selected))

    elif index == 7:
        option_selected = select_option(loyalty_points_options_x, loyalty_points_options_y)
        print("Selected loyalty point option: {}".format(option_selected))

    elif index == 9:
        option_selected = select_option(auctions_options_x, auctions_options_y)
        print("Selected auctions option: {}".format(option_selected))

def select_option(x_coordinates, y_coordinates):

    time.sleep(2)

    index: int = random.randint(0, len(x_coordinates) - 1)

    pyautogui.moveTo(x_coordinates[index], y_coordinates[index], duration=1)

    recheck()

    time.sleep(1)

    pyautogui.click()

    time.sleep(1)

    recheck()

    return index

def handle_vpn():

    pyautogui.moveTo(1697, 79, duration=1)
    pyautogui.click()

    time.sleep(1)

    pyautogui.moveTo(1463, 272, duration=1)
    pyautogui.click()

    while True:
        screenshot = ImageGrab.grab()
        color = screenshot.getpixel((1482, 309))

        if color == (128, 209, 251):
            break

        time.sleep(2)

    pyautogui.moveTo(1538, 191, duration=1)
    pyautogui.click()

    while True:

        pyautogui.moveTo(1447, 258, duration=1)
        pyautogui.click()
        pyautogui.write("")

        country = vpn_countries[random.randint(0, len(vpn_countries) - 1)]
        pyautogui.write(country)

        screenshot = ImageGrab.grab()
        color = screenshot.getpixel((1588, 393))

        if color == (217, 217, 221) or color == (255, 255, 255):

            pyautogui.moveTo(1588, 393, duration=1)
            pyautogui.click()
            print("VPN connected successfully to {}".format(country))
            break

        else:
            continue

def open_chatbot():
    move_wait_click(1814, 956, (147, 17, 126))
    recheck()

def wait_for_options():

    print("Waiting for options...")
    pyautogui.moveTo(1724, 676, duration=1)

    start_time = time.time()
    count = 0

    while True:

        if start_time == 0:
            start_time = time.time()

        screenshot = ImageGrab.grab()
        color = screenshot.getpixel((1724, 676))
        if color == (88, 180, 202):
            break

        if (time.time() - start_time) > 10:
            start_time = 0
            count += 1

        recheck()
        if count >= 2:
            pyautogui.moveTo(1556, 861, duration=1)
            recheck()
            pyautogui.click()
            count = 0
            time.sleep(1)

if __name__ == "__main__":
    main()
