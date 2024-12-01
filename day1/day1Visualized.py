import tkinter as tk
import time
from threading import Thread


class PairingApp:
    def __init__(self, root, left_list, right_list):
        self.root = root
        self.left_list = left_list
        self.right_list = right_list
        self.sorted_left = sorted(left_list)
        self.sorted_right = sorted(right_list)

        self.root.title("Pairing Animation")
        self.root.geometry("1000x600")
        self.root.config(bg="black")

        # Canvas for animation
        self.canvas = tk.Canvas(self.root, width=1000, height=500, bg="black", highlightthickness=0)
        self.canvas.pack()

        # Info Label
        self.info_label = tk.Label(self.root, text="", font=("Arial", 16), bg="black", fg="white")
        self.info_label.pack()

        # Buttons for Part 1 and Part 2
        self.part1_button = tk.Button(self.root, text="Part 1", command=self.start_part1, font=("Arial", 14))
        self.part1_button.pack(side=tk.LEFT, padx=20)

        self.part2_button = tk.Button(self.root, text="Part 2", command=self.start_part2, font=("Arial", 14))
        self.part2_button.pack(side=tk.RIGHT, padx=20)

        # Restart Button (Hidden Initially)
        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_app, font=("Arial", 14))
        self.restart_button.pack(pady=20)
        self.restart_button.pack_forget()

        # Hold references to drawn elements
        self.left_band_items = []
        self.right_band_items = []
        self.connecting_line = None

    def draw_timeline(self, current_index, total_distance=None, similarity_score=None):
        """Update the timeline-style visualization to avoid flickering."""
        # Band dimensions
        band_height = 100
        margin = 20
        visible_range = 20  # Show up to 20 pairs at a time
        start_index = max(0, current_index - visible_range // 2)
        end_index = min(len(self.left_list), start_index + visible_range)

        # Update left band
        self.update_band(
            self.left_band_items,
            self.left_list[start_index:end_index],
            margin,
            100,
            band_height,
            current_index,
            start_index,
            visible_range,
        )

        # Update right band
        self.update_band(
            self.right_band_items,
            self.right_list[start_index:end_index],
            margin,
            300,
            band_height,
            current_index,
            start_index,
            visible_range,
        )

        # Draw or update connecting line
        if self.connecting_line:
            self.canvas.delete(self.connecting_line)

        if current_index < len(self.left_list):
            left_x = margin + (current_index - start_index) * 45 + 20
            right_x = left_x  # Both bands scroll together
            self.connecting_line = self.canvas.create_line(
                left_x, 200, right_x, 300, fill="yellow", width=2
            )

        # Update info label
        if total_distance is not None:
            self.info_label.config(
                text=f"Current Pair: {self.sorted_left[current_index]} <-> {self.sorted_right[current_index]} | Total Distance: {total_distance}"
            )
        elif similarity_score is not None:
            self.info_label.config(
                text=f"Current Number: {self.sorted_left[current_index]} | Matches: {self.right_list.count(self.sorted_left[current_index])} | Similarity Score: {similarity_score}"
            )

    def update_band(self, band_items, values, margin, y_offset, band_height, current_index, start_index, visible_range):
        """Update a band (top or bottom) without clearing the canvas."""
        # Remove extra items if the visible range shrinks
        while len(band_items) > len(values) * 2:  # Each value has a rectangle and a text
            item = band_items.pop()
            self.canvas.delete(item)

        # Update existing items or add new ones
        for i, num in enumerate(values):
            x = margin + i * 45
            color = "green" if (start_index + i) <= current_index else "gray"

            # Update or create rectangle
            if i * 2 < len(band_items):  # Rectangle
                self.canvas.itemconfig(band_items[i * 2], fill=color)
                self.canvas.coords(band_items[i * 2], x, y_offset, x + 40, y_offset + band_height)
            else:
                rect = self.canvas.create_rectangle(
                    x, y_offset, x + 40, y_offset + band_height, fill=color, outline=""
                )
                band_items.append(rect)

            # Update or create text
            if i * 2 + 1 < len(band_items):  # Text
                self.canvas.coords(band_items[i * 2 + 1], x + 20, y_offset + band_height // 2)
                self.canvas.itemconfig(band_items[i * 2 + 1], text=str(num))
            else:
                text = self.canvas.create_text(
                    x + 20, y_offset + band_height // 2, text=str(num), font=("Arial", 10), fill="white"
                )
                band_items.append(text)

    def start_part1(self):
        """Start Part 1 animation."""
        self.part1_button.pack_forget()
        self.part2_button.pack_forget()
        Thread(target=self.animate_part1, daemon=True).start()

    def start_part2(self):
        """Start Part 2 animation."""
        self.part1_button.pack_forget()
        self.part2_button.pack_forget()
        Thread(target=self.animate_part2, daemon=True).start()

    def animate_part1(self):
        """Animate Part 1."""
        total_distance = 0
        for i in range(len(self.sorted_left)):
            distance = abs(self.sorted_left[i] - self.sorted_right[i])
            total_distance += distance
            self.draw_timeline(i, total_distance=total_distance)
            time.sleep(0.1)

        self.info_label.config(text=f"Part 1 Complete! Total Distance: {total_distance}", font=("Arial", 20, "bold"))
        self.restart_button.pack()

    def animate_part2(self):
        """Animate Part 2."""
        similarity_score = 0
        for i in range(len(self.sorted_left)):
            matches = self.right_list.count(self.sorted_left[i])
            similarity_score += self.sorted_left[i] * matches
            self.draw_timeline(i, similarity_score=similarity_score)
            time.sleep(0.1)

        self.info_label.config(
            text=f"Part 2 Complete! Total Similarity Score: {similarity_score}", font=("Arial", 20, "bold")
        )
        self.restart_button.pack()

    def restart_app(self):
        """Restart the app."""
        self.restart_button.pack_forget()
        self.info_label.config(text="")
        self.part1_button.pack(side=tk.LEFT, padx=20)
        self.part2_button.pack(side=tk.RIGHT, padx=20)
        self.canvas.delete("all")
        self.left_band_items.clear()
        self.right_band_items.clear()
        self.connecting_line = None

file = "c:\\Users\\thebo\\repos\\AoC2024\\day1\\day1.txt"
with open(file) as f:
    content = f.readlines()
content = [x.strip() for x in content]

l = []
r = []

for line in content:
    line = line.split("   ")
    #print(line)
    l.append(int(line[0]))
    r.append(int(line[1]))
print(l,r)
l = sorted(l)
r = sorted(r)


# Create and run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = PairingApp(root, l, r)
    root.mainloop()
