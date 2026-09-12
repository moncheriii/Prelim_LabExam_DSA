class Song:
    def __init__(self, song_id: str, title: str, artist: str, duration: str):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"[{self.song_id}] {self.title} - {self.artist} ({self.duration})"


class Node:
    def __init__(self, song: Song):
        self.song = song
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self._count = 0

    def isEmpty(self) -> bool:
        return self.head is None

    def size(self) -> int:
        return self._count

    def insertFirst(self, song: Song):
        new_node = Node(song)
        new_node.next = self.head
        self.head = new_node
        self._count += 1
        print(f"Success: '{song.title}' added at the beginning of the playlist.")

    def insertLast(self, song: Song):
        new_node = Node(song)
        if self.isEmpty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._count += 1
        print(f"Success: '{song.title}' added at the end of the playlist.")

    def insertAt(self, position: int, song: Song):
        if position < 1 or position > self._count + 1:
            print(f"Error: Position must be between 1 and {self._count + 1}.")
            return

        if position == 1:
            self.insertFirst(song)
            return

        new_node = Node(song)
        current = self.head
        for _ in range(1, position - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self._count += 1
        print(f"Success: '{song.title}' inserted at position {position}.")

    def display(self):
        if self.isEmpty():
            print("\nThe playlist is currently empty.")
            return

        print("\n--- MUSIC PLAYLIST ---")
        current = self.head
        position = 1
        while current:
            print(f"{position}. {current.song}")
            current = current.next
            position += 1
        print(f"Total Songs: {self._count}")

    def search(self, song_id: str):
        current = self.head
        position = 1
        while current:
            if current.song.song_id.lower() == song_id.lower():
                return current.song, position
            current = current.next
            position += 1
        return None, -1

    def delete(self, song_id: str):
        if self.isEmpty():
            print("Error: Playlist is empty.")
            return

        current = self.head
        prev = None

        while current:
            if current.song.song_id.lower() == song_id.lower():
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                self._count -= 1
                print(f"Success: Song '{current.song.title}' (ID: {song_id}) removed.")
                return
            prev = current
            current = current.next

        print(f"Error: Song with ID '{song_id}' not found.")


def main():
    playlist = SinglyLinkedList()
    choice = -1

    while choice != 8:
        print("\n==================================")
        print("      MUSIC PLAYLIST MANAGER      ")
        print("==================================")
        print("1. Add Song at Beginning")
        print("2. Add Song at End")
        print("3. Insert Song at Position")
        print("4. Display Playlist")
        print("5. Search Song")
        print("6. Remove Song")
        print("7. Display Playlist Size")
        print("8. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 8.")
            continue

        if choice in (1, 2, 3):
            if choice == 3 and playlist.isEmpty():
                print("Playlist is empty. Defaulting to position 1.")

            sid = input("Enter Song ID: ").strip()
            stitle = input("Enter Song Title: ").strip()
            sartist = input("Enter Artist: ").strip()
            sduration = input("Enter Duration (e.g., 3:45): ").strip()
            song = Song(sid, stitle, sartist, sduration)

            if choice == 1:
                playlist.insertFirst(song)
            elif choice == 2:
                playlist.insertLast(song)
            elif choice == 3:
                try:
                    pos = int(input("Enter position to insert: "))
                    playlist.insertAt(pos, song)
                except ValueError:
                    print("Invalid position input.")

        elif choice == 4:
            playlist.display()

        elif choice == 5:
            sid = input("Enter Song ID to search: ").strip()
            song, position = playlist.search(sid)
            if song:
                print(f"\nFound at position {position}: {song}")
            else:
                print(f"\nSong with ID '{sid}' not found.")

        elif choice == 6:
            sid = input("Enter Song ID to remove: ").strip()
            playlist.delete(sid)

        elif choice == 7:
            print(f"\nTotal Songs in Playlist: {playlist.size()}")

        elif choice == 8:
            print("Closing Music Playlist Manager. Thank you and Goodbye!")

        else:
            print("Invalid option! Select between 1 and 8.")


if __name__ == "__main__":
    main()