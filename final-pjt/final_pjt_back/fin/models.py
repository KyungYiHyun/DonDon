from django.db import models
from django.conf import settings

class DepositProducts(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,symmetrical=False,related_name='like_depositproducts')
    fin_co_no = models.TextField()
    fin_prdt_cd = models.TextField()
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    mtrt_int = models.TextField()
    etc_note = models.TextField()
    join_deny = models.TextField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()
    max_limit = models.TextField(null=True)
    fin_grp_cd = models.TextField()
    # 옵션 필드 추가
    intr_rate = models.FloatField()
    intr_rate_type = models.TextField()
    intr_rate_type_nm = models.TextField()
    intr_rate2 = models.FloatField(null=True)
    save_trm = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['fin_co_no','fin_prdt_cd','save_trm', 'intr_rate_type_nm','intr_rate','intr_rate2'], 
                name='unique_product_term_rate_type'
        )
    ]

class SavingProducts(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, symmetrical=False,related_name='like_savingproducts')
    fin_co_no = models.TextField()
    kor_co_nm = models.TextField()
    fin_prdt_cd = models.TextField()
    fin_prdt_nm = models.TextField()
    join_way = models.TextField(null=True)
    mtrt_int = models.TextField()
    spcl_cnd = models.TextField()
    join_deny = models.TextField()
    join_member = models.TextField()
    etc_note = models.TextField()
    max_limit = models.TextField(null=True)
    fin_grp_cd = models.TextField()
    intr_rate_type = models.TextField()
    intr_rate_type_nm = models.TextField()
    rsrv_type = models.TextField()
    rsrv_type_nm = models.TextField()
    save_trm = models.TextField()
    intr_rate = models.TextField()
    intr_rate2 = models.TextField()
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['fin_co_no','fin_prdt_cd','save_trm', 'intr_rate_type_nm','intr_rate','intr_rate2'], 
                name='unique_product_term_rate_type2'
        )
    ]