# Visitor interface
class Visitor:
    def visit_text_file(self, file):
        pass

    def visit_image_file(self, file):
        pass

    def visit_video_file(self, file):
        pass

# Concrete visitor: PrintVisitor
class PrintVisitor(Visitor):
    def visit_text_file(self, file):
        print("Printing text file:", file.name)

    def visit_image_file(self, file):
        print("Printing image file:", file.name)

    def visit_video_file(self, file):
        print("Printing video file:", file.name)

# Concrete visitor: EditVisitor
class EditVisitor(Visitor):
    def visit_text_file(self, file):
        print("Editing text file:", file.name)

    def visit_image_file(self, file):
        print("Editing image file:", file.name)

    def visit_video_file(self, file):
        print("Editing video file:", file.name)

# File interface
class File:
    def accept(self, visitor):
        pass

# Concrete file: TextFile
class TextFile(File):
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        visitor.visit_text_file(self)

# Concrete file: ImageFile
class ImageFile(File):
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        visitor.visit_image_file(self)

# Concrete file: VideoFile
class VideoFile(File):
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        visitor.visit_video_file(self)

# Usage
files = [TextFile("document.txt"), ImageFile("image.jpg"), VideoFile("video.mp4")]

print_visitor = PrintVisitor()
edit_visitor = EditVisitor()

for file in files:
    file.accept(print_visitor)

for file in files:
    file.accept(edit_visitor)
