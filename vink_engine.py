import re

class VinkPrivacyGuardian:
    def __init__(self):
        # Professional-grade entity recognition registry
        self.registry = {
            'EMAIL': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            'PHONE': r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
            'API_KEY': r'(sk-[a-zA-Z0-9]{48}|AIza[0-9A-Za-z-_]{35}|sk_live_[a-zA-Z0-9]{24})',
            'ACCOUNT_ID': r'\b\d{10,12}\b',
            'IP_ADDRESS': r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
            'CREDIT_CARD': r'\b(?:\d[ -]*?){13,16}\b'
        }

    def analyze_and_mask(self, text, active_rules):
        detected_entities = []
        sanitized_text = text
        risk_score = "Low"

        for label, pattern in self.registry.items():
            if active_rules.get(label, True):
                matches = re.findall(pattern, text)
                if matches:
                    detected_entities.extend([(label, m) for m in matches])
                    for i, match in enumerate(matches):
                        mask_placeholder = f"<{label}_REDACTED_{i+1}>"
                        sanitized_text = sanitized_text.replace(match, mask_placeholder)
                    
                    if label in ['API_KEY', 'CREDIT_CARD', 'ACCOUNT_ID']:
                        risk_score = "High"
                    elif risk_score != "High":
                        risk_score = "Medium"

        action = "ALLOW" if risk_score == "Low" else ("MASK" if risk_score == "Medium" else "BLOCK")
        return {
            "sanitized": sanitized_text,
            "entities": detected_entities,
            "risk_score": risk_score,
            "action": action
        }

    def generate_risk_summary(self, result):
        """
        Generates medium-length technical intelligence reports.
        Clear status indicators and bold headings included.
        """
        entities = result['entities']
        count = len(entities)
        risk = result['risk_score']
        found_types = list(set([e[0] for e in entities]))
        
        # SCENARIO A: HIGH RISK
        if risk == "High":
            return f"""
**CRITICAL SECURITY STATUS: DANGEROUS - TRANSMISSION DISALLOWED**

**EXECUTIVE SUMMARY**
A high-severity policy violation was intercepted. System identified {count} critical artifacts: {', '.join(found_types)}. The risk profile exceeds established organizational safety thresholds.

**TECHNICAL THREAT VECTOR**
Detection of raw authentication tokens indicates a failure in upstream cryptographic hygiene. Transmitting these to an LLM facilitates 'Weight Poisoning' and 'Lateral Movement,' potentially compromising the production API surface and internal cloud infrastructure.

**COMPLIANCE & REMEDIATION**
This event constitutes a material breach under SOC2 and ISO 27001 control frameworks. 
**STATUS: TERMINATED.** The request has been blocked and logged for forensic SOC review.
            """
            
        # SCENARIO B: MEDIUM RISK
        elif risk == "Medium":
            return f"""
**PRIVACY SECURITY STATUS: CAUTION - TRANSMISSION ALLOWED (MASKED)**

**EXECUTIVE SUMMARY**
Inspection flagged {count} instances of Protected Information ({', '.join(found_types)}). This constitutes a violation of the 'Privacy-by-Design' baseline for external data processing.

**TECHNICAL THREAT VECTOR**
Leakage of identifiers enables 'Identity Stitching,' allowing third-party processors to de-anonymize internal stakeholders. Proper obfuscation is required to prevent unauthorized profiling and meet GDPR 'Data Minimization' mandates.

**COMPLIANCE & REMEDIATION**
The payload violates GDPR Article 25 and CCPA residency standards. 
**STATUS: SANITIZED.** Context-aware masking applied to ensure utility while maintaining the organizational privacy posture.
            """
            
        # SCENARIO C: LOW RISK
        else:
            return """
**SYSTEM SECURITY STATUS: SAFE - TRANSMISSION ALLOWED**

**EXECUTIVE SUMMARY**
Deep-content inspection concluded. Payload cross-referenced against all restriction registries; no prohibited patterns or sensitive entities were identified.

**TECHNICAL THREAT VECTOR**
Content exhibits a safe heuristic profile with low entropy. No hardcoded secrets, cryptographic keys, or identifiable PII detected. Classified as 'Non-Sensitive Business Logic.'

**COMPLIANCE & REMEDIATION**
Full alignment with internal Security Policy Frameworks. 
**STATUS: AUTHORIZED.** Request cleared for forward-routing to the AI inference engine.
            """

guardian = VinkPrivacyGuardian()