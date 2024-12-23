# NewLab3
Bu script sap.aztu.edu.az saytına daxil olur. Daha sonra istifadəçidən ad və parol istəyir. Ardında "Tələbə" hissəsinə keçid edir. Fənnlər hissəsində "Python proqramlaşdırma dili" dərsini seçir. Daha sonra isə davamiyyət hissəsindən dərsdə iştirak edib etmədiyini yoxlayır və nəticələri .txt faylına yazır.
# Davamiyyət Yoxlama Sistemi

Bu script, Selenium və BeautifulSoup kitabxanalarından istifadə edərək sap.aztu.edu.az  davamiyyət məlumatlarını avtomatik olaraq toplayır. İstifadəçi daxil olduqdan sonra, "Davamiyyet" bölməsinə keçərək dərsə qatılma statusunu oxuyur və bu məlumatları `log_davamiyyet.txt` faylında saxlayır.

## Tələblər

Bu skriptin işləməsi üçün aşağıdakı Python kitabxanaları lazımdır:

- selenium==4.6.0
- beautifulsoup4==4.12.0
- webdriver-manager==3.8.0

## Quraşdırma

Layihəni işlətməyə başlamaq üçün əvvəlcə virtual mühit yaratmaq, asılılıqları quraşdırmaq və skripti işə salmaq lazımdır.

### 1. Virtual Mühit Yaratmaq

Virtual mühit yaratmaq, layihənizi izolyasiya edilmiş bir mühitdə işlətmək üçün yaxşı bir təcrübədir. Aşağıdakı addımları izləyin:

1. **Virtual mühit yaratmaq:**

   Layihə qovluğuna daxil olduqdan sonra aşağıdakı əmri işlədin:

   ```bash
   python -m venv venv

2. **Virtual mühiti aktivləşdirmək:**

   Windows : ```
   python -m venv venv```
   
   Mac/Linux: ```source venv/bin/activate```


### 2. Asılılıqları Quraşdırmaq

Virtual mühit aktiv olduqdan sonra, layihə üçün tələb olunan Python paketlərini quraşdırmaq lazımdır. Bunun üçün aşağıdakı əmri işlədin:

   ```bash
  pip install -r requirements.txt
```

### 3.Skripti İşlətmək
Asılılıqlar quraşdırıldıqdan sonra, skripti işə salmaq üçün aşağıdakı əmri yazın:
  ```bash
  python script-adı.py

```
Bu əmrlə skript işləməyə başlayacaq və davamiyyət məlumatlarını toplayacaq. Toplanan məlumatlar log_davamiyyet.txt faylında saxlanacaq.








      

