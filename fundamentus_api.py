import csv
import io
import flask
import requests
from bs4 import BeautifulSoup
from flask_restful import Resource, Api

app = flask.Flask(__name__)
api = Api(app)

class GetData(object):

    def __init__(self, p):
        self.table = []
        self.papel = p
    
    def get_data(self):
        self.papel = self.papel.rstrip()
        url = "https://www.fundamentus.com.br/detalhes.php?papel="+self.papel
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')

        dia = self.cleaner(self.corrigir(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(2) .data:nth-child(2) .oscil font"))))
        mes = self.cleaner(self.corrigir(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(3) .data:nth-child(2) .oscil font"))))
        trinta_dias = self.cleaner(self.corrigir(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(4) .data:nth-child(2) .oscil font"))))
        doze_meses = self.cleaner(self.corrigir(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(5) .data:nth-child(2) .oscil font"))))
        vinte = self.cleaner(self.corrigir(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(6) .data:nth-child(2) .oscil font"))))
        dezenove = self.cleaner(self.corrigir(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(7) .data:nth-child(2) .oscil font"))))
        dezoito = self.cleaner(self.corrigir(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(8) .data:nth-child(2) .oscil font"))))
        dezesete = self.cleaner(self.corrigir(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(9) .data:nth-child(2) .oscil font"))))
        dezeseis = self.cleaner(self.corrigir(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(10) .data:nth-child(2) .oscil font"))))
        quinze = self.cleaner(self.corrigir(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(11) .data:nth-child(2) .oscil font"))))
        p_l = self.cleaner(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(2) .data:nth-child(4) .txt")))
        p_vp= self.cleaner(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(3) .data:nth-child(4) .txt")))
        p_ebit= self.cleaner(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(4) .data:nth-child(4) .txt")))
        psr= self.cleaner(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(5) .data:nth-child(4) .txt")))
        p_ativos = self.cleaner(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(6) .data:nth-child(4) .txt")))
        p_cap_giro = self.cleaner(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(7) .data:nth-child(4) .txt")))
        p_ativ_circ_liq= self.cleaner(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(8) .data:nth-child(4) .txt")))
        dy= self.cleaner(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(9) .data:nth-child(4) .txt")))
        ev_ebitida= self.cleaner(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(10) .data:nth-child(4) .txt")))
        ev_ebit= self.cleaner(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(11) .data:nth-child(4) .txt")))
        cresc_rec= self.cleaner(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(12) .data:nth-child(4) .txt")))
        lpa = self.cleaner(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(2) .data:nth-child(6) .txt")))
        vpa = self.cleaner(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(3) .data:nth-child(6) .txt")))
        marg_bruta = self.cleaner(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(4) .data:nth-child(6) .txt")))
        marg_ebit = self.cleaner(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(5) .data:nth-child(6) .txt")))
        marg_liq = self.cleaner(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(6) .data:nth-child(6) .txt")))
        ebit_ativo = self.cleaner(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(7) .data:nth-child(6) .txt")))
        roic = self.cleaner(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(8) .data:nth-child(6) .txt")))
        roe = self.cleaner(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(9) .data:nth-child(6) .txt")))
        liqu_corr = self.cleaner(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(10) .data:nth-child(6) .txt")))
        divBr_patrim = self.cleaner(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(11) .data:nth-child(6) .txt")))
        giro_ativos = self.cleaner(str(soup.select(".center .clearfix .w728:nth-child(4) tr:nth-child(12) .data:nth-child(6) .txt")))

        try:
            self.table.append([self.papel, dia, mes, trinta_dias, doze_meses,vinte ,dezenove,dezoito, dezesete, dezeseis, quinze, p_l, p_vp, p_ebit, psr, p_ativos, p_cap_giro, p_ativ_circ_liq, dy, ev_ebitida, ev_ebit, 
            cresc_rec, lpa, vpa, marg_bruta, marg_ebit, marg_liq,ebit_ativo, roic, roe, liqu_corr, divBr_patrim, giro_ativos])
            return "Dados Encontrados", 302
        except:
            return "Ausência de dados", 417
    
    def cleaner(self, linha):
        valor = ""
        for i in linha:
            if i.isdigit() or i == "," or i == "-":
                valor = valor+i
        return valor
 
    def corrigir(self, n):
        valor = ""
        check = False
        for i in n:
            if i == ">":
                check = True
            if check == True:
                valor = valor + i
        return valor
    
    def export_csv(self):
        gaveta = [["","DIA (%)","MÊS (%)","30DIAS (%)","12MESES (%)","2020 (%)","2019 (%)","2018 (%)","2017 (%)","2016 (%)","2015 (%)","P/L","P/VP","P/EBIT","PSR", "P/ATIVOS","P/CAP. GIRO","P/ATIV CIRC LIQ","DIV. YIELD (%)","EV/EBITIDA","EV/EBIT",
        "CRESC. REC (5A) (%)","LPA","VPA","MARG.BRUTA (%)","MARG.EBIT (%)","MARG.LÍQUIDA (%)","EBIT/ATIVO (%)","ROIC (%)","ROE (%)","LIQUIDEZ CORR","DIV BR/PATRIM","GIRO ATIVOS"]]
        for i in self.table:
            gaveta.append(i)
        
        si = io.StringIO()
        writer = csv.writer(si)
        for i in gaveta:
            writer.writerow(i)
        
        return [si.getvalue(), 200]



class ApiRoutes(Resource):
    def get(self, papel):
        scraper = GetData(papel.upper())
        response, status = scraper.get_data()
        if status == 302:
            response, status = scraper.export_csv()

        response = flask.make_response(response, status)
        response.headers.set('content-type', 'text/csv')
        response.headers.set('Content-Disposition', 'attachment', filename=papel+'.csv')
        return response


api.add_resource(ApiRoutes, "/<string:papel>")

if __name__ == '__main__':
    app.run()
