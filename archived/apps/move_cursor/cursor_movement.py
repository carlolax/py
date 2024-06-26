import math
import numpy as np
import pyautogui
import time

def get_random_offsets(num_moves: int) -> np.ndarray:
    return np.random.randint(-10, 11, size=(num_moves, 2))

def get_horizontal_offsets() -> np.ndarray:
    return np.vstack(([-10, 0], [10, 0]))

def get_vertical_offsets() -> np.ndarray:
    return np.vstack(([0, -10], [0, 10]))

def get_circular_offset(radius: int, angle: float) -> tuple[int, int]:
    x_offset = int(radius * math.cos(angle))
    y_offset = int(radius * math.sin(angle))
    return x_offset, y_offset

def move_cursor(x_offset: int, y_offset: int, duration: float) -> None:
    try:
        pyautogui.move(x_offset, y_offset, duration=duration)
    except pyautogui.PyAutoGUIException as exception:
        print(f"An error occurred while moving the cursor: {exception}")

def choose_cursor_movement_type(random_offsets, horizontal_offsets, vertical_offsets, radii, angles, i):
    choice: str = np.random.choice(["random", "horizontal", "vertical", "circular"])
    if choice == "random":
        return random_offsets[i]
    elif choice == "horizontal":
        return horizontal_offsets[i % 2]
    elif choice == "vertical":
        return vertical_offsets[i % 2]
    elif choice == "circular":
        return get_circular_offset(radii[i], angles[i])

def move_cursor_like_person(num_moves: int) -> None:
    random_offsets = get_random_offsets(num_moves)
    horizontal_offsets = get_horizontal_offsets()
    vertical_offsets = get_vertical_offsets()
    angles = np.random.uniform(0, 2 * np.pi, num_moves)
    radii = np.random.randint(5, 21, size=num_moves)
    
def move_cursor_like_person(num_moves: int) -> None:
    random_offsets = get_random_offsets(num_moves)
    horizontal_offsets = get_horizontal_offsets()
    vertical_offsets = get_vertical_offsets()
    angles = np.random.uniform(0, 2 * np.pi, num_moves)
    radii = np.random.randint(5, 21, size=num_moves)

    # Precompute values that are not dependent on the loop iteration
    durations = np.random.uniform(0.001, 0.05, num_moves)
    sleeps = np.random.uniform(0.01, 0.1, num_moves)

    for i in range(num_moves):
        try:
            x_offset, y_offset = choose_cursor_movement_type(random_offsets, horizontal_offsets, vertical_offsets, radii, angles, i)
            move_cursor(x_offset, y_offset, durations[i])
            time.sleep(sleeps[i])
        except pyautogui.FailSafeException as failsafe_error:
            print(f"A failsafe error occurred: {failsafe_error}. Retrying...")
            # Add logic to retry
        except pyautogui.PyAutoGUIException as autogui_error:
            print(f"An error occurred while moving the cursor: {autogui_error}")
            # Log the error for further analysis
        except Exception as exception:
            print(f"An unexpected error occurred: {exception}")
            # Log the error for further analysis
