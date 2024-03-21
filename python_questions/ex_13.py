"""
Załóżmy że poniższy pseudokod tworzy obiekt singletona:

funkcja Singleton getInstance() {
if (instancja_obiektu_Singleton nie istnieje) {
 instancja_obiektuSingleton = stwórz Singleton()   }
 return instancja_obiektu_Singleton
}

Dodatkowo istnieją 2 wątki jednego procesu, które niezależnie od siebie wykonują funkcję  getInstance().
Ile maksymalnie instancji obiektu Singleton zostanie utworzonych w najbardziej pesymistycznym scenariuszu?

"""
'dwie?'
