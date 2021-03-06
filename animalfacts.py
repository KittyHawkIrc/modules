import random

#Update schema
__url__ = "https://raw.githubusercontent.com/KittyHawkIrc/modules/production/" + __name__ + ".py"
__version__ = 1.0

factimg = [
  "https://i.sli.mg/ohFHK6.png",
  "https://i.sli.mg/ELRYvY.png",
  "https://i.sli.mg/69q0D6.png",
  "https://i.sli.mg/O6FoBq.png",
  "https://i.sli.mg/4BwmmO.png",
  "https://i.sli.mg/yiF1Dx.png",
  "https://i.sli.mg/uXfU31.jpg",
  "https://i.sli.mg/UdVNJw.png",
  "https://i.sli.mg/UT4Jtw.png",
  "https://i.sli.mg/3WbUYA.jpg",
  "https://i.sli.mg/3WbUYA.jpg",
  "https://i.sli.mg/er1srJ.png",
  "https://i.sli.mg/6zypyK.png",
  "https://i.sli.mg/EY9kKt.png",
  "https://i.sli.mg/pVZSxp.png",
  "https://i.sli.mg/zuxPeR.png",
  "https://i.sli.mg/sFgUw5.png",
  "https://i.sli.mg/78kk44.jpg",
  "https://i.sli.mg/e0HN0J.jpg",
  "https://i.sli.mg/vTzonq.jpg",
  "https://i.sli.mg/Hf4VP5.jpg",
  "https://i.sli.mg/z8CjFW.jpg",
  "https://i.sli.mg/0G4U5B.jpg",
  "https://i.sli.mg/VFSAbo.jpg",
  "https://i.sli.mg/UZDeCl.jpg",
  "https://i.sli.mg/Og0VO7.jpg",
  "https://i.sli.mg/JeNU2X.jpg",
  "https://i.sli.mg/uRv5sZ.jpg",
  "https://i.sli.mg/51cgRA.jpg",
  "https://i.sli.mg/Qjg6eM.jpg",
  "https://i.sli.mg/4VuWx1.jpg",
  "https://i.sli.mg/clVwG0.png",
  "https://i.sli.mg/7BaNWd.png",
  "https://i.sli.mg/3RktOS.png",
  "https://i.sli.mg/ZIEt7Y.png",
  "https://i.sli.mg/AAZdPC.png",
  "https://i.sli.mg/vgCPHp.png",
  "https://i.sli.mg/iHqk9S.png",
  "https://i.sli.mg/sCwzmV.png",
  "https://i.sli.mg/foI3Ky.png",
  "https://i.sli.mg/zDTzzI.png",
  "https://i.sli.mg/j6vRWK.png",
  "https://i.sli.mg/3grCFZ.png",
  "https://i.sli.mg/nc7Ctv.png",
  "https://i.sli.mg/KKqxy6.png",
  "https://i.sli.mg/nf8ZyN.png",
  "https://i.sli.mg/2ETKZP.png",
  "https://i.sli.mg/rweVPd.png",
  "https://i.sli.mg/HFJTWA.png",
  "https://i.sli.mg/ZUaxnu.png",
  "https://i.sli.mg/tMUJS8.png",
  "https://i.sli.mg/va4Ktf.png",
  "https://i.sli.mg/w4tsAa.png",
  "https://i.sli.mg/sbLsoA.png",
  "https://i.sli.mg/5YeYyN.jpg",
  "https://i.sli.mg/WxM7Ql.jpg",
  "https://i.sli.mg/IEZNzO.jpg",
  "https://i.sli.mg/j4GPCm.jpg",
  "https://i.sli.mg/8UYEul.jpg",
  "https://i.sli.mg/Hftq8p.jpg",
  "https://i.sli.mg/zJJiNu.jpg",
  "https://i.sli.mg/gdWzh0.jpg",
  "https://i.sli.mg/Cozyq2.jpg",
  "https://i.sli.mg/HSs2a0.jpg",
  "https://i.sli.mg/TzuXuA.jpg",
  "https://i.sli.mg/NGnoMO.jpg",
  "https://i.sli.mg/RaHYMa.jpg",
  "https://i.sli.mg/MzdYoZ.jpg",
  "https://i.sli.mg/zdOm7R.jpg",
  "https://i.sli.mg/4cYfX9.jpg",
  "https://i.sli.mg/zjWFVg.jpg",
  "https://i.sli.mg/kcNO9k.jpg",
  "https://i.sli.mg/tQhXA4.jpg",
  "https://i.sli.mg/WIhOvC.jpg",
  "https://i.sli.mg/Gx7mVA.jpg",
  "https://i.sli.mg/HMbvnc.jpg",
  "https://i.sli.mg/iyvCz6.jpg",
  "https://i.sli.mg/JanAP2.jpg",
  "https://i.sli.mg/Lrqk0Q.jpg",
  "https://i.sli.mg/ioulWo.jpg",
  "https://i.sli.mg/v6Tyw7.jpg",
  "https://i.sli.mg/t1BHXr.jpg",
  "https://i.sli.mg/aJFtPO.jpg",
  "https://i.sli.mg/mNxKcj.jpg",
  "https://i.sli.mg/ySRGeM.jpg",
  "https://i.sli.mg/fx9WmM.jpg",
  "https://i.sli.mg/nZTT1Z.jpg",
  "https://i.sli.mg/PB0rpn.jpg",
  "https://i.sli.mg/knfflM.jpg",
  "https://i.sli.mg/bSEDZu.jpg",
  "https://i.sli.mg/gWzssX.jpg",
  "https://i.sli.mg/X1bts2.jpg",
  "https://i.sli.mg/7bbg2y.jpg",
  "https://i.sli.mg/pW5VfJ.jpg",
  "https://i.sli.mg/3SCAkM.jpg",
  "https://i.sli.mg/MuXHs1.jpg",
  "https://i.sli.mg/nIqjSO.jpg",
  "https://i.sli.mg/ibcjgy.jpg",
  "https://i.sli.mg/Rdh91N.jpg",
  "https://i.sli.mg/migpI4.jpg",
  "https://i.sli.mg/cWCEYN.jpg",
  "https://i.sli.mg/Ec72MX.jpg",
  "https://i.sli.mg/GNsB8j.jpg",
  "https://i.sli.mg/VOAu7w.jpg",
  "https://i.sli.mg/8tA7dJ.jpg",
  "https://i.sli.mg/FKnSJL.jpg",
  "https://i.sli.mg/vwh09R.jpg",
  "https://i.sli.mg/7hfNL5.jpg",
  "https://i.sli.mg/ERVaw4.jpg",
  "https://i.sli.mg/kaIVRi.jpg",
  "https://i.sli.mg/Si5OY0.jpg",
  "https://i.sli.mg/B85v27.jpg",
  "https://i.sli.mg/5ypvSp.jpg",
  "https://i.sli.mg/vSIvk7.jpg",
  "https://i.sli.mg/7tfnJA.jpg",
  "https://i.sli.mg/T6CRO5.jpg",
  "https://i.sli.mg/V2fbRs.png",
  "https://i.sli.mg/XVkzvE.jpg",
  "https://i.sli.mg/lRXChF.jpg",
  "https://i.sli.mg/kwIweF.jpg",
  "https://i.sli.mg/aU2HCK.jpg",
  "https://i.sli.mg/akmo6Q.jpg",
  "https://i.sli.mg/BFOwOJ.jpg",
  "https://i.sli.mg/uI8HbM.jpg",
  "https://i.sli.mg/29AaSf.jpg"
]

def declare():
  return {"animalfacts": "privmsg", "sadanimalfacts": "privmsg"}

def callback(self):
  try:
    if self.message.split(' ')[1] == "new":
      return self.msg(self.channel, "Here's the newest sad animal fact! %s" % ('http://i.imgur.com/WfhlfQR.jpg'))
  except:
    pass
  return self.msg(self.channel, "Here's a sad animal fact for you! %s" % ('http://i.imgur.com/WfhlfQR.jpg'))

class api:
  def msg(self, channel, text):
    return "[%s] %s" % (channel, text)

if __name__ == "__main__":
  api = api()
  setattr(api, 'isop', True)
  setattr(api, 'type', 'privmsg')
  setattr(api, 'command', 'animalfacts')
  setattr(api, 'user', 'joe!username@hostmask')
  setattr(api, 'channel', "#test")
  setattr(api, 'message', '^animalfacts')

  if "Here\'s a" not in callback(api):
    system.exit(1)
  setattr(api, 'message', '^animalfacts new')
  if "Here\'s the" not in callback(api):
    exit(2)
