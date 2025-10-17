ROTEIRO_FRAUDE = {
    "FASE_1_CONTEXTO_CRITICO": {
        "Desafios Específicos": [
            "Desbalanceamento extremo (< 0.1% fraudes)",
            "Padrões em constante evolução",
            "Custo assimétrico (FN >> FP)",
            "Requisito de tempo real"
        ],
        "Premissas": [
            "Velocidade > Perfeição (tempo real)",
            "Recall inicial > Precision (capturar fraudes)",
            "Adaptabilidade contínua (modelos dinâmicos)"
        ]
    },
    
    "FASE_2_ABORDAGEM_MULTICAMADAS": {
        "Estratégia em Camadas": [
            "1. Regras simples (velocity checks, geolocation)",
            "2. ML não-supervisionado (detecção de anomalias)", 
            "3. ML supervisionado (classificação refinada)"
        ],
        "Features Temporais": [
            "Comportamento sazonal (horário, dia semana)",
            "Histórico recente (transações últimas 24h)",
            "Padrões de gasto (valor, frequência, local)"
        ]
    },
    
    "FASE_3_SELECAO_MODELOS": {
        "Modelos por Cenário": [
            "Isolation Forest: poucos dados labeled, novas fraudes",
            "Random Forest: dados históricos balanced",
            "XGBoost: performance máxima + customização"
        ],
        "Tratamento Desbalanceamento": [
            "SMOTE/ADASYN (synthetic samples)",
            "Class weights (algorithm level)",
            "Ensemble methods (balanced bags)"
        ]
    },
    
    "FASE_4_VALIDACAO_TEMPORAL": {
        "Problema Data Leakage": [
            "Split temporal obrigatório (não random)",
            "Time Series Cross-Validation",
            "Backtesting com dados históricos"
        ],
        "Métricas Específicas": [
            "F2-Score (foco no recall)",
            "Precision-Recall AUC (melhor que ROC)",
            "Custo monetário (FN*custo_fraude + FP*custo_cliente)"
        ]
    },
    
    "FASE_5_SISTEMA_PRODUCAO": {
        "Arquitetura em Tempo Real": [
            "Streaming processing (Kafka, Spark)",
            "Model scoring em < 100ms",
            "Sistema de fallback (regras)"
        ],
        "Sistema de Resposta": [
            "Bloqueio automático (alto risco)",
            "Autenticação adicional (médio risco)", 
            "Monitoramento (baixo risco)"
        ],
        "Feedback Loop": [
            "Confirmação de fraudes (ground truth)",
            "Retreinamento automático",
            "Detecção de concept drift"
        ]
    }
}