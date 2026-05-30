import re

def count_clauses_and_print_first_sentences(contract):
    # 1) 条項の開始パターンで分割
    clause_pattern = r'(\d+\.\s)'
    parts = re.split(clause_pattern, contract)
    
    # 2) 分割結果から条項を再構成
    clauses = []
    for i in range(1, len(parts), 2):
        header = parts[i]                  # 例: "1. "
        body = parts[i+1].strip() if i+1 < len(parts) else ""
        clauses.append(header + body)
    
    # 3) 条項数を出力
    num_clauses = len(clauses)
    if num_clauses == 0:
        return
    print(num_clauses)
    
    # 4) 各条項の最初の文を取り出して表示
    for clause in clauses:
        # 最初のピリオド位置を探す
        dot_pos = clause.find('.')
        if dot_pos != -1:
            rest = clause[dot_pos+1:]
            # 次のピリオドまでを抽出
            next_dot = rest.find('.')
            if next_dot != -1:
                first_sentence = clause[:dot_pos+1+next_dot+1].strip()
            else:
                first_sentence = clause.strip()
        else:
            first_sentence = clause.strip()
        print(first_sentence)

# ハードコードされた契約テキスト
contract_text = (
    "1. This Agreement is made between the parties. It sets forth the terms and conditions. "
    "2. The duration of the Agreement is one year. Extensions are subject to mutual consent. "
    "3. Termination may occur with thirty days' notice. Obligations survive termination."
)

count_clauses_and_print_first_sentences(contract_text)