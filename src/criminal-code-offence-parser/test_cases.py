"""
Test cases for the Criminal Code Offence Parser.
This script runs through various offence types to verify correct parsing and reporting.
"""

from main import report

def run_test_cases():
    """Run through all test cases and generate reports."""
    
    print("\n=== Running Criminal Code Offence Parser Test Cases ===\n")

    # Category 1: Life Sentences (255 years)
    print("\n--- Testing Life Sentences ---")
    print("\nTesting High Treason (should show life sentence):")
    report("cc_46(1)")
    print("\nTesting Breaking and Entering with Intent (should show life sentence):")
    report("cc_348(1)(d)")

    # Category 2: SOIRA Registration
    print("\n--- Testing SOIRA Registration ---")
    print("\nTesting Sexual Assault (primary SOIRA offence):")
    report("cc_271")
    print("\nTesting Extortion (SOIRA with life maximum):")
    report("cc_346(1.1)(b)")

    # Category 3: Hybrid Offences
    print("\n--- Testing Hybrid Offences ---")
    print("\nTesting Sexual Assault (different minimums):")
    report("cc_271")
    print("\nTesting Dangerous Operation - First Offence (fine minimums):")
    report("cc_320.13(2)-1")
    print("\nTesting Dangerous Operation - Subsequent (escalating minimums):")
    report("cc_320.13(2)-s")

    # Category 4: DNA Orders
    print("\n--- Testing DNA Orders ---")
    print("\nTesting Break and Enter - Dwelling (primary DNA):")
    report("cc_348(1)(d)")
    print("\nTesting Assaulting Peace Officer (secondary DNA):")
    report("cc_270")

    # Category 5: Weapons Prohibitions
    print("\n--- Testing Weapons Prohibitions ---")
    print("\nTesting Possession of Prohibited Firearm (mandatory prohibition):")
    report("cc_95")
    print("\nTesting Armed Robbery - First Offence (firearm provisions):")
    report("cc_344(1)(a)-1")

    # Category 6: Criminal Organization Offences
    print("\n--- Testing Criminal Organization Offences ---")
    print("\nTesting Possessing Explosives - Criminal Organization:")
    report("cc_82(2)")
    print("\nTesting Armed Robbery - Criminal Org - Subsequent:")
    report("cc_344(1)(a)-s")

    # Category 7: Fine-Only Offences
    print("\n--- Testing Fine-Only Offences ---")
    print("\nTesting Failure to Comply with SOIRA (fine-only):")
    report("cc_490.031")
    print("\nTesting Assisting Deserter (summary only):")
    report("cc_54")

    # Category 8: Mandatory Minimums
    print("\n--- Testing Mandatory Minimums ---")
    print("\nTesting Dangerous Operation - Second Offence (30 days min):")
    report("cc_320.13(2)-2")
    print("\nTesting Armed Robbery - Subsequent (7 years min):")
    report("cc_344(1)(a)-s")

    # Category 9: Section 469 Offences
    print("\n--- Testing Section 469 Offences ---")
    print("\nTesting Treason:")
    report("cc_46(2)")
    print("\nTesting Piracy:")
    report("cc_74")

    print("\n=== Test Cases Complete ===")
    print("\nNote: Review the output above to verify that:")
    print("1. Life sentences are properly formatted")
    print("2. SOIRA registrations show correct durations")
    print("3. Hybrid offences show both summary and indictable options")
    print("4. DNA orders are correctly identified")
    print("5. Weapons prohibitions are properly noted")
    print("6. Criminal organization provisions are recognized")
    print("7. Fine-only offences are properly handled")
    print("8. Mandatory minimums are clearly displayed")
    print("9. Section 469 offences are properly identified")

if __name__ == "__main__":
    run_test_cases()
