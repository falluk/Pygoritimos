#Carregando a Base

pip install pandas

import pandas as pd

base = pd.read_excel("2018_abr_jun.xlsx", encoding="ISO-8859-1",error_bad_lines=False)

base

coll_descricao = base.Descrição

#Configuração


conf = coll_descricao.str.findall('Configuração')
conf2 = coll_descricao.str.findall('configuração')
conf3 = coll_descricao.str.findall('Configuraçao')
conf4 = coll_descricao.str.findall('configuraçao')
conf5 = coll_descricao.str.findall('Configuracão')
conf6 = coll_descricao.str.findall('configuracão')
conf7 = coll_descricao.str.findall('Configuracao')
conf8 = coll_descricao.str.findall('configuracao')


cont_conf1 = len(conf.sum())
cont_conf2= len(conf2.sum())
cont_conf3 = len(conf3.sum())
cont_conf4= len(conf4.sum())
cont_conf5 = len(conf5.sum())
cont_conf6= len(conf6.sum())
cont_conf7 = len(conf7.sum())
cont_conf8= len(conf8.sum())

count_conf_total = cont_conf1 + cont_conf2 + cont_conf3 + cont_conf4 + cont_conf5 + cont_conf6 + cont_conf7 + cont_conf8

count_conf_total

#Instalação

inst1 = coll_descricao.str.findall('Instalação')
inst2 = coll_descricao.str.findall('instalação')
inst3 = coll_descricao.str.findall('Instalaçao')
inst4 = coll_descricao.str.findall('instalaçao')
inst5 = coll_descricao.str.findall('Instalacão')
inst6 = coll_descricao.str.findall('instalacão')
inst7 = coll_descricao.str.findall('Instalacao')
inst8 = coll_descricao.str.findall('instalacao')


cont_inst1 = len(inst1.sum())
cont_inst2= len(inst2.sum())
cont_inst3 = len(inst3.sum())
cont_inst4= len(inst4.sum())
cont_inst5 = len(inst5.sum())
cont_inst6= len(inst6.sum())
cont_inst7 = len(inst7.sum())
cont_inst8= len(inst8.sum())

count_inst_total = cont_inst1 + cont_inst2 + cont_inst3 + cont_inst4 + cont_inst5 + cont_inst6 + cont_inst7 + cont_inst8

count_inst_total

#Computador não liga


pc_n_liga1 = coll_descricao.str.findall('não liga')
pc_n_liga2 = coll_descricao.str.findall('computador desligado')
pc_n_liga3 = coll_descricao.str.findall('computador não liga')

cont_pc_n_liga1 = len(pc_n_liga1.sum())
cont_pc_n_liga2 = len(pc_n_liga2.sum())
cont_pc_n_liga3 = len(pc_n_liga3.sum())

pc_n_liga_total = cont_pc_n_liga1 + cont_pc_n_liga2 + cont_pc_n_liga3

pc_n_liga_total

#Lentidão

pc_lento1 = coll_descricao.str.findall('computador lendo')
pc_lento2 = coll_descricao.str.findall('lentidão')
pc_lento3 = coll_descricao.str.findall('Desktop lento')
pc_lento4 = coll_descricao.str.findall('lentidao')

cont_pc_lento1 = len(pc_lento1.sum())
cont_pc_lento2 = len(pc_lento2.sum())
cont_pc_lento3 = len(pc_lento3.sum())
cont_pc_lento4 = len(pc_lento4.sum())

cont_pc_lento_total = cont_pc_lento1 + cont_pc_lento2 + cont_pc_lento3 + cont_pc_lento4

cont_pc_lento_total

#Impressora

imp1 = coll_descricao.str.findall('Impressora')
imp2 = coll_descricao.str.findall('impressora')
imps = coll_descricao.str.findall('Impressora:')

cont_imp1 = len(imp1.sum())
cont_imp2 = len(imp2.sum())
cont_imps = len(imps.sum())


impressora = cont_imp1 + cont_imp2  + cont_imps

impressora

#Impressora Lis

imp_lis1 = coll_descricao.str.findall('lis')
imp_lis2 = coll_descricao.str.findall('Lis')
imp_lis3 = coll_descricao.str.findall('impressora lis')
imp_lis4 = coll_descricao.str.findall('impressora Lis')

cont_imp_lis1 = len(imp_lis1.sum())
cont_imp_lis2 = len(imp_lis2.sum())
cont_imp_lis3 = len(imp_lis3.sum())
cont_imp_lis4 = len(imp_lis4.sum())

impressora_lis = cont_imp_lis1 + cont_imp_lis2 + cont_imp_lis3 + cont_imp_lis4

impressora_lis

#PDA

pda1 = coll_descricao.str.findall('pda')
pda2 = coll_descricao.str.findall('PDA')

cont_pda1 = len(pda1.sum())
cont_pda2 = len(pda2.sum())

pda_total = cont_pda1 + cont_pda2

pda_total

#Smartphone

cel1 = coll_descricao.str.findall('Smartphone')
cel2 = coll_descricao.str.findall('smartphone')
cel3 = coll_descricao.str.findall('celular')
cel4 = coll_descricao.str.findall('Celular')

cont_cel1 = len(cel1.sum())
cont_cel2 = len(cel2.sum())
cont_cel3 = len(cel3.sum())
cont_cel4 = len(cel4.sum())

cel_total = cont_cel1 + cont_cel2 + cont_cel3 + cont_cel4

cel_total

#Notebook

note1 = coll_descricao.str.findall('Notebook')
note2 = coll_descricao.str.findall('notebook')

cont_note1 = len(note1.sum())
cont_note2 = len(note2.sum())

notebooks = cont_note1 + cont_note2

notebooks

