import pymysql

class DatabaseMysql:
    
    def koneksi(self):
        kon = pymysql.connect('localhost','root','root','belajar_2') # ganti sesuai parameter koneksi ke db
        return kon
    
    def create_siawa(self,nama,kelas,jurusan,tempat_lahir,tgl_lahir):
        db = self.koneksi()
        kur = db.cursor()
        sql = "insert siswa values(0,'%s','%s','%s','%s','%s')"%(nama,kelas,jurusan,tempat_lahir,tgl_lahir)
        try:
            kur.execute(sql)
            db.commit()
        except Exception as e:
            print('Maaf penyimpanan gagal')
            print(e)
        finally:
            db.close()
    
    def delete_siswa(self,id):
        db = self.koneksi()
        kur = db.cursor()
        sql = "delete from siswa where id = %d"%(id)
        try:
            kur.execute(sql)
            db.commit()
        except Exception as e:
            print('Maaf penghapusan gagal')
            print(e)
        finally:
            db.close()
    
    def update_siswa(self,nama,id):
        db = self.koneksi()
        kur = db.cursor()
        sql = "update siswa set nama = '%s' where id = %d"%(nama,id)
        try:
            kur.execute(sql)
            db.commit()
        except Exception as e:
            print('Maaf pembaran gagal')
            print(e)
        finally:
            db.close()
    
    def get_siswa(self):
        db = self.koneksi()
        kur = db.cursor(pymysql.cursors.DictCursor)
        sql = "select * from siswa"
        kur.execute(sql)
        result = kur.fetchall()
        return result
