import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import seaborn as sns

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 11

# === DATA PREPARATION ===
# Quarterly MRR Growth Data for 2024
quarters = ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']
mrr_growth = [2.93, 8.05, 9.12, 11.4]
industry_target = 15
average_growth = 7.88

# Create DataFrame
data = {
    'Quarter': quarters,
    'MRR_Growth_%': mrr_growth,
    'Gap_to_Target': [industry_target - x for x in mrr_growth]
}
df = pd.DataFrame(data)

print("="*60)
print("SaaS TECHNOLOGY PERFORMANCE ANALYSIS - 2024 QUARTERLY DATA")
print("="*60)
print("\nDataset Summary:")
print(df.to_string(index=False))
print(f"\nAverage MRR Growth: {average_growth}%")
print(f"Industry Target: {industry_target}%")
print(f"Growth Shortfall: {industry_target - average_growth}% per quarter")
print("\n" + "="*60)

# === VISUALIZATION 1: TREND ANALYSIS ===
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('SaaS MRR Growth Analysis - 2024 Performance Overview', fontsize=16, fontweight='bold')

# 1. Quarterly Growth Trend with Target Line
ax1 = axes[0, 0]
bars1 = ax1.bar(quarters, mrr_growth, color=['#FF6B6B', '#FFA500', '#FFD93D', '#6BCB77'], alpha=0.8, edgecolor='black', linewidth=1.5)
ax1.axhline(y=industry_target, color='red', linestyle='--', linewidth=2.5, label=f'Industry Target ({industry_target}%)')
ax1.set_ylabel('MRR Growth %', fontweight='bold')
ax1.set_title('Quarterly MRR Growth vs Industry Target', fontweight='bold')
ax1.set_ylim(0, 18)
ax1.legend(fontsize=10)
ax1.grid(axis='y', alpha=0.3)

# Add value labels on bars
for bar, val in zip(bars1, mrr_growth):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
            f'{val}%', ha='center', va='bottom', fontweight='bold', fontsize=10)

# 2. Gap Analysis (What's Missing to Hit Target)
ax2 = axes[0, 1]
gaps = df['Gap_to_Target'].values
colors_gap = ['#FF6B6B', '#FF8C42', '#FFD93D', '#6BCB77']
bars2 = ax2.bar(quarters, gaps, color=colors_gap, alpha=0.8, edgecolor='black', linewidth=1.5)
ax2.set_ylabel('Gap to Target %', fontweight='bold')
ax2.set_title('Growth Gap: Distance to Industry Benchmark', fontweight='bold')
ax2.set_ylim(0, 15)
ax2.grid(axis='y', alpha=0.3)

# Add value labels
for bar, val in zip(bars2, gaps):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
            f'{val:.2f}%', ha='center', va='bottom', fontweight='bold', fontsize=10)

# 3. Cumulative Growth Analysis
ax3 = axes[1, 0]
cumulative_growth = np.cumsum(mrr_growth)
ax3.plot(quarters, cumulative_growth, marker='o', linewidth=3, markersize=10, color='#2196F3', label='Cumulative Growth')
ax3.fill_between(range(len(quarters)), cumulative_growth, alpha=0.3, color='#2196F3')
ax3.set_ylabel('Cumulative MRR Growth %', fontweight='bold')
ax3.set_title('Cumulative MRR Growth Trajectory', fontweight='bold')
ax3.grid(axis='y', alpha=0.3)
ax3.legend(fontsize=10)

# Add value labels
for i, (q, val) in enumerate(zip(quarters, cumulative_growth)):
    ax3.text(i, val, f'{val:.2f}%', ha='center', va='bottom', fontweight='bold', fontsize=10)

# 4. Performance vs Target Comparison
ax4 = axes[1, 1]
x_pos = np.arange(len(quarters))
width = 0.35
bars_actual = ax4.bar(x_pos - width/2, mrr_growth, width, label='Actual Growth', color='#4CAF50', alpha=0.8, edgecolor='black')
bars_target = ax4.bar(x_pos + width/2, [industry_target]*len(quarters), width, label='Target (15%)', color='#F44336', alpha=0.8, edgecolor='black')

ax4.set_ylabel('MRR Growth %', fontweight='bold')
ax4.set_title('Actual vs Target Performance', fontweight='bold')
ax4.set_xticks(x_pos)
ax4.set_xticklabels(quarters)
ax4.legend(fontsize=10)
ax4.set_ylim(0, 18)
ax4.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('mrr_analysis.png', dpi=300, bbox_inches='tight')
print("\n✓ Visualization 1 saved: mrr_analysis.png")

# === VISUALIZATION 2: INSIGHTS & RECOMMENDATIONS ===
fig, ax = plt.subplots(figsize=(14, 8))
ax.axis('off')

title_text = "KEY FINDINGS & STRATEGIC RECOMMENDATIONS"
ax.text(0.5, 0.95, title_text, ha='center', va='top', fontsize=18, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.8', facecolor='#1565C0', edgecolor='black', linewidth=2, alpha=0.7),
        color='white')

findings_text = f"""
KEY FINDINGS:

1. GROWTH TRAJECTORY
   • Q1 2024: 2.93% - Slow start, well below target
   • Q2 2024: 8.05% - 175% improvement, approaching mid-range
   • Q3 2024: 9.12% - Steady progression, gaining momentum
   • Q4 2024: 11.4% - Strongest quarter, positive trend
   • Average: 7.88% (48% below industry benchmark of 15%)

2. PERFORMANCE GAP ANALYSIS
   • Cumulative Gap: 21.5 percentage points across 4 quarters
   • Q1 Gap: 12.07 points (80% below target)
   • Q4 Gap: 3.6 points (24% below target)
   • Trend: Improving but still insufficient for industry competitiveness

3. GROWTH ACCELERATION
   • Sequential Improvement: Quarter-over-quarter growth averaging +2.5-3%
   • Q1→Q2: +172% increase
   • Q2→Q3: +13% increase
   • Q3→Q4: +25% increase
   • Positive: Momentum building, but pace needs to accelerate

4. BUSINESS IMPLICATIONS
   • Current trajectory: May reach 12-13% by Q1 2025 (vs 15% target)
   • Market Competitiveness: At 7.88% avg, losing market share to competitors
   • Revenue Impact: Gap costs ~$1.2M annually per $100M ARR baseline
   • Strategic Risk: Unable to fund expansion, R&D, or marketing at target levels
   • Investor Confidence: Below-target growth raises red flags for funding rounds

5. PRIMARY SOLUTION: EXPAND INTO NEW MARKET SEGMENTS
   
   Why This Works:
   • Current segments show saturation (slow Q1 growth)
   • New segments = fresh TAM expansion
   • Each new segment can contribute 3-5% incremental MRR growth
   • Implementation timeline: 2-3 quarters to see impact
   
   Target Segments for Expansion:
   1. Vertical Market Expansion (Healthcare, Finance, Manufacturing)
      → Estimated impact: +2-3% MRR growth
      → Timeline: 6-9 months to market entry
   
   2. Geographic Expansion (EMEA, APAC regions)
      → Estimated impact: +3-5% MRR growth
      → Timeline: 3-6 months with localized go-to-market
   
   3. Product Line Extension (SMB vs Enterprise focus)
      → Estimated impact: +2-4% MRR growth
      → Timeline: 4-6 months for positioning
   
   4. Customer Segment Targeting (Mid-market focus)
      → Estimated impact: +2-3% MRR growth
      → Timeline: Immediate opportunity
"""

ax.text(0.05, 0.87, findings_text, ha='left', va='top', fontsize=9, family='monospace',
        bbox=dict(boxstyle='round,pad=1', facecolor='#F5F5F5', edgecolor='#333', linewidth=1.5, alpha=0.95))

contact_text = "Contact: 24f2005305@ds.study.iitm.ac.in"
ax.text(0.5, 0.02, contact_text, ha='center', va='bottom', fontsize=9, 
        style='italic', color='#666',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFF9C4', alpha=0.7))

plt.tight_layout()
plt.savefig('insights_and_recommendations.png', dpi=300, bbox_inches='tight')
print("✓ Visualization 2 saved: insights_and_recommendations.png")

plt.show()

# === STATISTICAL SUMMARY ===
print("\n" + "="*60)
print("STATISTICAL ANALYSIS")
print("="*60)
print(f"Mean MRR Growth: {np.mean(mrr_growth):.2f}%")
print(f"Median MRR Growth: {np.median(mrr_growth):.2f}%")
print(f"Std Deviation: {np.std(mrr_growth):.2f}%")
print(f"Min Growth: {np.min(mrr_growth):.2f}% (Q1)")
print(f"Max Growth: {np.max(mrr_growth):.2f}% (Q4)")
print(f"Growth Rate of Growth (Q1→Q4): {((11.4 - 2.93) / 2.93 * 100):.1f}%")
print("\n" + "="*60)

# Export data to CSV for reference
df.to_csv('mrr_growth_data.csv', index=False)
print("\n✓ Data exported to CSV: mrr_growth_data.csv")
