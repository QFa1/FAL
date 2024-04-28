from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PIL import Image, ImageFilter, ImageDraw
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtMultimedia
from PyQt5 import uic
import requests
import sys


class FAL(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('FAL.ui', self)  # Загрузка дизайна
        self.setWindowTitle('FAL')
        self.initUI()

    def initUI(self):  # Программа
        self.FALimg = 'images/new.jpg'
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]  # Выбор нужного фото
        self.pixmap = QPixmap(self.fname)
        self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)  # конвертирование фото под нужный размер

        # Конект кнопок с их функциями
        self.exit.clicked.connect(self.exitapp)
        self.red.clicked.connect(self.redcolor)
        self.green.clicked.connect(self.greencolor)
        self.blue.clicked.connect(self.bluecolor)
        self.all.clicked.connect(self.allfunc)
        self.leftButton.clicked.connect(self.left)
        self.rightButton.clicked.connect(self.right)
        self.saveas.clicked.connect(self.saveasfunc)
        self.save.clicked.connect(self.savefunc)
        self.openfile.clicked.connect(self.open)
        self.urlbutton.clicked.connect(self.urlfunc)

        # Конект кнопок с 1-ой таблички "Фильтры"
        self.blackwhite.clicked.connect(self.b_and_w)
        self.blackwhite2.clicked.connect(self.b_and_w2)
        self.greenery.clicked.connect(self.greeneryfunc)
        self.night.clicked.connect(self.nightfunc)
        self.sunset.clicked.connect(self.sunsetfunc)
        self.sky.clicked.connect(self.skyfunc)
        self.pervansh.clicked.connect(self.pervanshfunc)
        self.flowers.clicked.connect(self.flowersfunc)
        self.fog.clicked.connect(self.fogfunc)
        self.arctic.clicked.connect(self.arcticfunc)
        self.radiashion.clicked.connect(self.radiashionfunc)
        self.kobalt.clicked.connect(self.kobaltfunc)
        self.greentoblue.clicked.connect(self.greentobluefunc)
        self.chestnut.clicked.connect(self.chestnutfunc)
        self.huji.clicked.connect(self.hujifunc)
        self.pumpkin.clicked.connect(self.pumpkinfunc)
        # Конект кнопок со 2-ой таблички "Эффекты"
        self.blur.clicked.connect(self.blurfunc)
        self.steopatra.clicked.connect(self.steopatrafunc)
        self.mirror.clicked.connect(self.mirrorfunc)
        self.invershion.clicked.connect(self.invershionfunc)
        self.invershiongrey.clicked.connect(self.invershiongreyfunc)
        self.contour.clicked.connect(self.contourfunc)
        self.emboss.clicked.connect(self.embossfunc)
        self.edges.clicked.connect(self.edgesfunc)
        self.smooth.clicked.connect(self.smoothfunc)
        self.maxfilter.clicked.connect(self.maxfunc)
        self.minfilter.clicked.connect(self.minfunc)

        # Конект кнопок с 3-ей таблички "Дополнительно"
        self.medium.clicked.connect(self.mediumfunc)
        self.cut.clicked.connect(self.cutfunc)
        self.size.clicked.connect(self.sizefunc)
        self.opposite.clicked.connect(self.oppositefunc)

        # Конект слайдеров с их функциями с 1-ой таблички "Фильтры"
        self.greenslider.valueChanged[int].connect(self.slidergreen)
        self.redslider.valueChanged[int].connect(self.sliderred)
        self.blueslider.valueChanged[int].connect(self.sliderblue)
        # Конект слайдеров с их функциями со 2-ой таблички "Эффекты"
        self.blurslider.valueChanged[int].connect(self.blursliderfunc)
        self.steopatraslider.valueChanged[int].connect(self.steopatrasliderfunc)
        # Конект слайдеров с их функциями со 3-ей таблички "Дополнительно"
        self.cutslider.valueChanged[int].connect(self.cutsliderfunc)

        # Музыка
        self.music_1('music/music1.mp3')
        self.music_2('music/music2.mp3')
        self.music_3('music/music3.mp3')
        self.music_4('music/music4.mp3')
        self.music_5('music/music5.mp3')
        self.music_6('music/music6.mp3')
        self.music_7('music/music7.mp3')
        # Кнопки музыки
        self.pause.clicked.connect(self.pause_)
        self.stop.clicked.connect(self.stop_)
        self.music1.clicked.connect(self.player1.play)
        self.music2.clicked.connect(self.player2.play)
        self.music3.clicked.connect(self.player3.play)
        self.music4.clicked.connect(self.player4.play)
        self.music5.clicked.connect(self.player5.play)
        self.music6.clicked.connect(self.player6.play)
        self.music7.clicked.connect(self.player7.play)

        # Отображение фото в программе
        try:
            self.image.setPixmap(self.pixmap1)
            im = Image.open(self.fname)
            im.save(self.FALimg)
        except AttributeError:
            self.fname = 'FALPhoto.jpg'
            self.otchet.setText('❗ Откройте фото ❗')

    def stop_(self):  # Стоп музыки
        self.player1.stop()
        self.player2.stop()
        self.player3.stop()
        self.player4.stop()
        self.player5.stop()
        self.player6.stop()
        self.player7.stop()
        self.otchet2.setText('Музыка остановлена')

    def pause_(self):  # Пауза музыки
        self.player1.pause()
        self.player2.pause()
        self.player3.pause()
        self.player4.pause()
        self.player5.pause()
        self.player6.pause()
        self.player7.pause()
        self.otchet2.setText('Пауза')

    def music_7(self, filename):  # 7-ая мелодия
        try:
            media = QtCore.QUrl.fromLocalFile(filename)
            content = QtMultimedia.QMediaContent(media)
            self.player7 = QtMultimedia.QMediaPlayer()
            self.player7.setMedia(content)
            self.otchet2.setText('')
        except AttributeError:
            pass

    def music_6(self, filename):  # 6-ая мелодия
        try:
            media = QtCore.QUrl.fromLocalFile(filename)
            content = QtMultimedia.QMediaContent(media)
            self.player6 = QtMultimedia.QMediaPlayer()
            self.player6.setMedia(content)
            self.otchet2.setText('')
        except AttributeError:
            pass

    def music_5(self, filename):  # 5-ая мелодия
        try:
            media = QtCore.QUrl.fromLocalFile(filename)
            content = QtMultimedia.QMediaContent(media)
            self.player5 = QtMultimedia.QMediaPlayer()
            self.player5.setMedia(content)
            self.otchet2.setText('')
        except AttributeError:
            pass

    def music_4(self, filename):  # 4-ая мелодия
        try:
            media = QtCore.QUrl.fromLocalFile(filename)
            content = QtMultimedia.QMediaContent(media)
            self.player4 = QtMultimedia.QMediaPlayer()
            self.player4.setMedia(content)
            self.otchet2.setText('')
        except AttributeError:
            pass

    def music_3(self, filename):  # 3-ая мелодия
        try:
            media = QtCore.QUrl.fromLocalFile(filename)
            content = QtMultimedia.QMediaContent(media)
            self.player3 = QtMultimedia.QMediaPlayer()
            self.player3.setMedia(content)
            self.otchet2.setText('')
        except AttributeError:
            pass

    def music_2(self, filename):  # 2-ая мелодия
        try:
            media = QtCore.QUrl.fromLocalFile(filename)
            content = QtMultimedia.QMediaContent(media)
            self.player2 = QtMultimedia.QMediaPlayer()
            self.player2.setMedia(content)
            self.otchet2.setText('')
        except AttributeError:
            pass

    def music_1(self, filename):  # 1-ая мелодия
        try:
            media = QtCore.QUrl.fromLocalFile(filename)
            content = QtMultimedia.QMediaContent(media)
            self.player1 = QtMultimedia.QMediaPlayer()
            self.player1.setMedia(content)
            self.otchet2.setText('')
        except AttributeError:
            pass

    def minfunc(self):  # Эффект Min Filter
        try:
            image = Image.open(self.FALimg)
            image2 = image.filter(ImageFilter.MinFilter(size=5))
            image2.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Эффект Min Filter применён')
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def maxfunc(self):  # Эффект Max Filter
        try:
            image = Image.open(self.FALimg)
            image2 = image.filter(ImageFilter.MaxFilter(size=5))
            image2.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Эффект Max Filter применён')
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def smoothfunc(self):  # Эффект Гладкость
        try:
            image = Image.open(self.FALimg)
            image2 = image.filter(ImageFilter.SMOOTH_MORE)
            image2.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Эффект Гладкость применён')
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def edgesfunc(self):  # Эффект края
        try:
            image = Image.open(self.FALimg)
            image2 = image.filter(ImageFilter.FIND_EDGES)
            image2.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Края фото найдены')
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def embossfunc(self):  # Эффект Тиснение
        try:
            image = Image.open(self.FALimg)
            image2 = image.filter(ImageFilter.EMBOSS)
            image2.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Эффект Тиснение применён')
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def contourfunc(self):  # Эффект контур
        try:
            image = Image.open(self.FALimg)
            image2 = image.filter(ImageFilter.CONTOUR)
            image2.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Контур применён ✅')
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def urlfunc(self):  # Открыть фото через адрес
        url = self.url.text()
        if url == '':
            self.otchet.setText('Вставьте ссылку')
        else:
            data = requests.get(url).content
            f = open(self.fname, 'wb')
            f.write(data)
            f.close()
            image2 = Image.open(self.fname)
            image2.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Фото открыто')

    def oppositefunc(self):  # Узнать противоположный цвет
        try:
            image = Image.open(self.FALimg)
            draw = ImageDraw.Draw(image)
            width = image.size[0]
            height = image.size[1]
            pix = image.load()
            for i in range(width):
                for j in range(height):
                    r, g, b = pix[i, j]
                    al = 255 - r, 255 - g, 255 - b
                    self.oppositenumb.setText(' RGB: ' + str(al))
            self.otchet.setText('Противоположный цвет')
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

        # Отображние среднего цвета фото рядом
        im = Image.new('RGB', (211, 41))
        draw = ImageDraw.Draw(im)
        draw.rectangle(((0, 0), (211, 41)), (255 - r, 255 - g, 255 - b))
        im.save('images/triangle2.png')
        self.pixmap = QPixmap('images/triangle2.png')
        self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
        self.oppositecolor.setPixmap(self.pixmap1)

    def sizefunc(self):  # Уменьшить размер фото
        try:
            x = self.sizex.text()
            y = self.sizey.text()
            im = Image.open(self.FALimg)
            im2 = im.resize((int(x), int(y)))
            im2.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(int(x), int(y), QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Уменьшен размер фото ✂')
        except ValueError:
            self.otchet.setText('❗ Вы не указали значения ❗')
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def cutsliderfunc(self, numb):  # Слайдер сокращения цветов
        self.b3 = 0
        self.procent3.setText(str(numb) + '%')
        # На сколько процентов слайдер продвинулся
        if numb == 0:
            self.b3 = 0
        elif 0 < numb <= 20:
            self.b3 = 20
        elif 20 < numb <= 40:
            self.b3 = 16
        elif 40 < numb <= 60:
            self.b3 = 12
        elif 60 < numb <= 80:
            self.b3 = 8
        elif 80 < numb <= 100:
            self.b3 = 4

    def cutfunc(self):  # Сократить цвета в фото
        try:
            im = Image.open(self.FALimg)
            im2 = im.quantize(self.b3)
            im2.save('images/8.bmp')
            self.pixmap = QPixmap('images/8.bmp')
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Цвета в фото уменьшены 🎨')
        except AttributeError:
            pass
        except ValueError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def greentobluefunc(self):  # Фильтр GB
        try:
            image = Image.open(self.fname)
            draw = ImageDraw.Draw(image)
            width = image.size[0]
            height = image.size[1]
            pix = image.load()
            for i in range(width):
                for j in range(height):
                    r, g, b = pix[i, j]
                    pix[i, j] = r, b, g
            image.save(self.FALimg, "JPEG")
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Применён фильтр GB 🟢➡️🔵')
        except TypeError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def kobaltfunc(self):  # Фильтр кобальт
        try:
            image = Image.open(self.fname)
            draw = ImageDraw.Draw(image)
            width = image.size[0]
            height = image.size[1]
            pix = image.load()
            for x in range(width):
                for y in range(height):
                    r = pix[x, y][0]
                    g = pix[x, y][1]
                    b = pix[x, y][2]
                    draw.point((x, y), (100 + r, 50 + g, 100 + b))
            image.save(self.FALimg, "JPEG")
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Применён фильтр Кобальт')
        except TypeError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def radiashionfunc(self):  # Фильтр радиация
        try:
            image = Image.open(self.fname)
            draw = ImageDraw.Draw(image)
            width = image.size[0]
            height = image.size[1]
            pix = image.load()
            for x in range(width):
                for y in range(height):
                    r = pix[x, y][0]
                    g = pix[x, y][1]
                    b = pix[x, y][2]
                    draw.point((x, y), (50 + r, 100 + g, 50 + b))
            image.save(self.FALimg, "JPEG")
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Применён фильтр Радиация ☢')
        except TypeError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def invershiongreyfunc(self):  # Инверсия оттенка серого
        try:
            image = Image.open(self.FALimg)
            draw = ImageDraw.Draw(image)
            width = image.size[0]
            height = image.size[1]
            pix = image.load()
            for x in range(width):
                for y in range(height):
                    r = pix[x, y][0]
                    g = pix[x, y][1]
                    b = pix[x, y][2]
                    sr = (r + g + b) // 3
                    draw.point((x, y), (255 - sr, 255 - sr, 255 - sr))
            image.save(self.FALimg, "JPEG")
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Применена инверсия серого 🔁')
        except TypeError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def invershionfunc(self):  # Инверсия фото
        try:
            image = Image.open(self.FALimg)  # Открываем изображение
            draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
            width = image.size[0]  # Определяем ширину
            height = image.size[1]  # Определяем высоту
            pix = image.load()
            for i in range(width):
                for j in range(height):
                    r, g, b = pix[i, j]
                    draw.point((i, j), (255 - r, 255 - g, 255 - b))
            image.save(self.FALimg, "JPEG")
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Применена инверсия фото 🔁')
        except TypeError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def mediumfunc(self):  # Узнаем средний цвет фото
        try:
            img = Image.open(self.FALimg)
            obj_for_count = img.load()
            f = open(self.FALimg, "rb")
            img_for_size = Image.open(f)
            f.close()
            sq = [0, 0, 0]
            count = img_for_size.size[0] * img_for_size.size[1]
            width = img_for_size.size[0]
            height = img_for_size.size[1]

            for i in range(width):
                for j in range(height):
                    sq[0] += obj_for_count[i, j][0]  # r
                    sq[1] += obj_for_count[i, j][1]  # g
                    sq[2] += obj_for_count[i, j][2]  # b
            out = [0, 0, 0]
            out[0] = int(sq[0] / count)
            out[1] = int(sq[1] / count)
            out[2] = int(sq[2] / count)
            al = out[0], out[1], out[2]
            self.mediumnumb.setText(' RGB: ' + str(al))  # Выводим средний цвет фото

            # Отображние среднего цвета фото рядом
            im = Image.new('RGB', (211, 41))
            draw = ImageDraw.Draw(im)
            draw.rectangle(((0, 0), (211, 41)), (out[0], out[1], out[2]))
            im.save('images/triangle.png')
            self.pixmap = QPixmap('images/triangle.png')
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.mediumcolor.setPixmap(self.pixmap1)
            self.otchet.setText('Средний цвет')
        except TypeError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def mirrorfunc(self):  # Отзеркаливание фото
        try:
            im = Image.open(self.FALimg)
            a = im.load()
            x, y = im.size
            xx = x // 2
            for i in range(xx):
                for j in range(y):
                    r, g, b = a[i, j]
                    rr, gg, bb = a[x - i - 1, j]
                    a[i, j] = rr, gg, bb
                    a[x - i - 1, j] = r, g, b
            im.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Фото отзеркалено ✅')
        except TypeError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def steopatrasliderfunc(self, numb):  # Слайдер эффекта стеопатра
        self.b2 = 0
        self.procent2.setText(str(numb) + '%')
        # На сколько процентов слайдер продвинулся
        if numb == 0:
            self.b2 = 0
        elif 0 < numb <= 20:
            self.b2 = 4
        elif 20 < numb <= 40:
            self.b2 = 8
        elif 40 < numb <= 60:
            self.b2 = 12
        elif 60 < numb <= 80:
            self.b2 = 16
        elif 80 < numb <= 100:
            self.b2= 20

    def steopatrafunc(self):  # Эффект стеопатра
        try:
            im = Image.open(self.FALimg)
            w, h = im.size
            im = im.convert('RGB')
            r, g, b = im.split()
            r_new = Image.new('L', (w, h))
            region = r.crop((0, 0, w - self.b2, h))
            r_new.paste(region, (self.b2, 0, w, h))
            im2 = Image.merge('RGB', (r_new, g, b))
            im2.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Применён эффект Стеопатра')
        except AttributeError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def blursliderfunc(self, numb):  # Слайдер эффекта заблюренности
        self.b = 0
        self.procent1.setText(str(numb) + '%')
        # На сколько процентов слайдер продвинулся
        if numb == 0:
            self.b = 0
        elif 0 < numb <= 20:
            self.b = 4
        elif 20 < numb <= 40:
            self.b = 8
        elif 40 < numb <= 60:
            self.b = 12
        elif 60 < numb <= 80:
            self.b = 16
        elif 80 < numb <= 100:
            self.b = 20

    def blurfunc(self):  # Эффект блюр
        try:
            image_file = Image.open(self.FALimg)
            image_file = image_file.filter(ImageFilter.BoxBlur(self.b))
            image_file.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Применён эффект Блюр 👀')
        except AttributeError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def arcticfunc(self):  # Фильтр Арктика
        try:
            im = Image.open(self.fname)
            layer = Image.new('RGB', im.size, 'white')
            output = Image.blend(im, layer, 0.2)
            output.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Применён фильтр Арктика ❄')
        except ValueError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def fogfunc(self):  # Фильтр туман
        try:
            im = Image.open(self.fname)
            layer = Image.new('RGB', im.size, 'white')
            output = Image.blend(im, layer, 0.3)
            output.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Применён фильтр Туман ‍🌫️')
        except ValueError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def flowersfunc(self):  # Фильтр цветы
        try:
            im = Image.open(self.fname)
            layer = Image.new('RGB', im.size, 'pink')
            output = Image.blend(im, layer, 0.2)
            output.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Применён фильтр Цветы 💐')
        except ValueError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def pervanshfunc(self):  # Фильтр перванш
        try:
            im = Image.open(self.fname)
            layer = Image.new('RGB', im.size, 'yellow')
            output = Image.blend(im, layer, 0.1)
            output.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Применён фильтр Перванш')
        except ValueError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def skyfunc(self):  # Фильтр небо
        try:
            im = Image.open(self.fname)
            layer = Image.new('RGB', im.size, 'blue')
            output = Image.blend(im, layer, 0.1)
            output.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Применён фильтр Небо 🌥')
        except ValueError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def sunsetfunc(self):  # Фильтр закат
        try:
            im = Image.open(self.fname)
            layer = Image.new('RGB', im.size, 'orange')
            output = Image.blend(im, layer, 0.1)
            output.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Применён фильтр Закат 🌅')
        except ValueError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def nightfunc(self):  # Фильтр ночь
        try:
            im = Image.open(self.fname)
            layer = Image.new('RGB', im.size, 'black')
            output = Image.blend(im, layer, 0.4)
            output.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Применён фильтр Ночь 🌙')
        except ValueError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def pumpkinfunc(self):  # Фильтр Тыква
        try:
            im = Image.open(self.fname)
            layer = Image.new('RGB', im.size, 'orange')
            output = Image.blend(im, layer, 0.4)
            output.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Применён фильтр Тыква 🎃')
        except ValueError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def hujifunc(self):  # Фильтр HUJI
        try:
            im = Image.open(self.fname)
            layer = Image.new('RGB', im.size, 'purple')
            output = Image.blend(im, layer, 0.1)
            output.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Применён фильтр HUJI')
        except ValueError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def chestnutfunc(self):  # Фильтр Каштан
        try:
            im = Image.open(self.fname)
            layer = Image.new('RGB', im.size, 'brown')
            output = Image.blend(im, layer, 0.2)
            output.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Применён фильтр Каштан')
        except ValueError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def greeneryfunc(self):  # Зеленоватый фильтр
        try:
            im = Image.open(self.fname)
            layer = Image.new('RGB', im.size, 'green')
            output = Image.blend(im, layer, 0.1)
            output.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Применён фильтр Зелень 🌿')
        except ValueError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def b_and_w2(self):  # черно-белая картинка №2
        try:
            image_file = Image.open(self.FALimg)
            image_file = image_file.convert("1")
            image_file.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Картинка черно-белая ⬛⬜')
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def b_and_w(self):  # черно-белая картинка
        try:
            image_file = Image.open(self.FALimg)
            image_file = image_file.convert("L")
            image_file.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Картинка черно-белая ⬛⬜')
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def open(self):  # Выбор нужного фото
        try:
            self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
            self.pixmap = QPixmap(self.fname)
            self.pixmap1 = self.pixmap.scaled(800, 560,
                                              QtCore.Qt.KeepAspectRatio)  # конвертирование фото под нужный размер
            self.image.setPixmap(self.pixmap1)
            im = Image.open(self.fname)
            im.save(self.FALimg)
            self.otchet.setText('Фото выбрано 🖼')
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')
        except AttributeError:
            self.otchet.setText('Фото не открыто :(')

    def savefunc(self):  # Сохранить фото
        try:
            im = Image.open(self.FALimg)
            im.save(self.fname)
            self.otchet.setText('Фото сохранено 💾')
        except ValueError:
            self.otchet.setText('❗ Откройте фото ❗')
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def saveasfunc(self):  # Сохранить фото как ...
        try:
            self.a = self.lineEdit.text()
            im = Image.open(self.FALimg)
            im.save(self.a)
            self.otchet.setText('Фото сохранено как ' + self.a + ' 💾')
        except ValueError:
            self.otchet.setText('Напишите название файла ❌')
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def greencolor(self):  # Зеленый цвет фото
        try:
            im = Image.open(self.FALimg)
            layer = Image.new('RGB', im.size, 'green')
            output = Image.blend(im, layer, 0.3)
            output.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Применён зелёный фильтр 🟢')
        except ValueError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def slidergreen(self, numb):  # Зеленый цвет фото слайдер
        a = 0
        # На сколько процентов слайдер продвинулся
        if numb == 0:
            a = 0
        elif 0 < numb <= 20:
            a = 0.2
        elif 20 < numb <= 40:
            a = 0.3
        elif 40 < numb <= 60:
            a = 0.4
        elif 60 < numb <= 80:
            a = 0.5
        elif 80 < numb <= 100:
            a = 0.6
        try:
            im = Image.open(self.fname)
            layer = Image.new('RGB', im.size, 'green')
            output = Image.blend(im, layer, a)
            output.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Применён зелёный фильтр 🟢')
        except ValueError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def redcolor(self):  # Красный цвет фото
        try:
            im = Image.open(self.FALimg)
            layer = Image.new('RGB', im.size, 'red')
            output = Image.blend(im, layer, 0.3)
            output.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Применён красный фильтр 🔴')
        except ValueError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def sliderred(self, numb):  # Красный цвет фото слайдер
        a = 0
        # На сколько процентов слайдер продвинулся
        if numb == 0:
            a = 0
        elif 0 < numb <= 20:
            a = 0.2
        elif 20 < numb <= 40:
            a = 0.3
        elif 40 < numb <= 60:
            a = 0.4
        elif 60 < numb <= 80:
            a = 0.5
        elif 80 < numb <= 100:
            a = 0.6
        try:
            im = Image.open(self.fname)
            layer = Image.new('RGB', im.size, 'red')
            output = Image.blend(im, layer, a)
            output.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Применён красный фильтр 🔴')
        except ValueError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def bluecolor(self):  # Синий цвет фото
        try:
            im = Image.open(self.FALimg)
            layer = Image.new('RGB', im.size, 'blue')
            output = Image.blend(im, layer, 0.3)
            output.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Применён синий фильтр 🔵')
        except ValueError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def sliderblue(self, numb):  # Синий цвет фото слайдер
        a = 0
        # На сколько процентов слайдер продвинулся
        if numb == 0:
            a = 0
        elif 0 < numb <= 20:
            a = 0.2
        elif 20 < numb <= 40:
            a = 0.3
        elif 40 < numb <= 60:
            a = 0.4
        elif 60 < numb <= 80:
            a = 0.5
        elif 80 < numb <= 100:
            a = 0.6
        try:
            im = Image.open(self.fname)
            layer = Image.new('RGB', im.size, 'blue')
            output = Image.blend(im, layer, a)
            output.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Применён синий фильтр 🔵')
        except ValueError:
            pass
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def allfunc(self):  # Сброс всех фильтров
        try:
            im = Image.open(self.fname)
            output = im
            output.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('Фото очищено 🧹')
        except AttributeError:
            self.otchet.setText('❗ Откройте новое фото ❗')
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def right(self):  # Поворот фото направо
        try:
            im = Image.open(self.FALimg)
            output = im.rotate(90)
            output.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('➡')
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def left(self):  # Поворот фото налево
        try:
            im = Image.open(self.FALimg)
            output = im.rotate(270)
            output.save(self.FALimg)
            self.pixmap = QPixmap(self.FALimg)
            self.pixmap1 = self.pixmap.scaled(800, 560, QtCore.Qt.KeepAspectRatio)
            self.image.setPixmap(self.pixmap1)
            self.otchet.setText('⬅')
        except FileNotFoundError:
            self.otchet.setText('❗ Откройте фото ❗')

    def exitapp(self):  # Выход из приложения
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FAL()
    ex.show()
    sys.exit(app.exec())
