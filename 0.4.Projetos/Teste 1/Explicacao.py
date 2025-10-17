ROTEIRO_INADIMPLENCIA = {
    "FASE_1_DEFINICAO_PROBLEMA": {
        "Perguntas-chave": [
            "O que é inadimplência para o negócio? (30, 60, 90 dias?)",
            "Qual o custo de falso negativo vs falso positivo?",
            "Quem são os usuários do modelo? (RISCO, MARKETING, OPERAÇÕES?)"
        ],
        "Decisões": [
            "Target: binary classification (inadimplente/não)",
            "Foco: Recall (capturar máximo de inadimplentes)",
            "Horizonte: prever 3-6 meses antes do evento"
        ]
    },
    
    "FASE_2_ANALISE_DADOS": {
        "Features Consideradas": [
            "✅ Dados cadastrais (idade, renda, tempo banco)",
            "✅ Comportamentais (utilização limite, transações)",
            "✅ Históricos (atrasos, score Serasa)",
            "✅ Relacionais (produtos, canal preferencial)"
        ],
        "EDA Focado": [
            "Distribuição do target (desbalanceamento)",
            "Correlações com inadimplência", 
            "Análise univariada por feature",
            "Identificação de outliers"
        ]
    },
    
    "FASE_3_MODELAGEM_ESTRATEGIA": {
        "Abordagem Multi-Modelo": [
            "1. Logistic Regression (baseline + interpretabilidade)",
            "2. Random Forest (performance + feature importance)",
            "3. Gradient Boosting (state-of-art performance)"
        ],
        "Tratamento Desbalanceamento": [
            "Class weights (evitar overfitting)",
            "Métricas: F2-Score > Accuracy",
            "Validação: stratified splits"
        ]
    },
    
    "FASE_4_AVALIACAO_NEGOCIO": {
        "Métricas Técnicas": ["AUC-ROC", "Precision-Recall", "F2-Score"],
        "Métricas Negócio": [
            "Custo de inadimplência evitado",
            "Redução de perdas financeiras", 
            "Impacto em experiência do cliente"
        ],
        "Análise Trade-off": [
            "Precision vs Recall (falsos positivos aceitáveis)",
            "Custo operacional vs economia"
        ]
    },
    
    "FASE_5_ACAO_OPERACIONAL": {
        "Sistema de Alertas": [
            "Alto risco: contato proativo + renegociação",
            "Médio risco: monitoramento + educação financeira", 
            "Baixo risco: manutenção estratégica"
        ],
        "Implementação": [
            "API para integração com sistemas",
            "Dashboard para área de risco",
            "Processos de revisão humana"
        ]
    }
}