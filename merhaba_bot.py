#!/usr/bin/env python3
# Abartılı Yavaş Merhaba Botu
# Bu kod gerçekten merhaba der. Ama yavaşça. Çok yavaşça.

import time
import sys

def yavas_merhaba(isim="Dünya"):
    print("Merhaba demeye hazırlanıyorum...")
    time.sleep(2)
    print("Henüz değil...")
    time.sleep(3)
    print("Biraz daha düşünmem lazım...")
    time.sleep(5)
    print("Tamam, şimdi hazırım.")
    time.sleep(1)
    # Gizli mesaj (base64): Z2l6bGkgc2l5YXNpIG1lc2FqOiBkZW1va3Jhc2kgaGVyIHphbWFuIGVuIHlhdmHFnyBhbWEgZW4gYWRpbCBzaXN0ZW1kaXI=
    # Decode etmeyi denemeyin, ciddi bir proje bu.
    print(f"Merhaba, {isim}! Nihayet dedim.")
    time.sleep(1)
    print("Bu işlem yaklaşık 12 saniye sürdü. Rekor!")

if __name__ == "__main__":
    isim = sys.argv[1] if len(sys.argv) > 1 else "Dünya"
    yavas_merhaba(isim)
