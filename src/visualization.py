import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Visualizer:
    def __init__(self, df: pd.DataFrame, output_dir: str):
        self.df = df
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        sns.set_theme(style="whitegrid")

    def plot_missing_values(self):
        plt.figure(figsize=(10, 6))
        missing = self.df.isnull().sum()
        missing = missing[missing > 0]
        if not missing.empty:
            missing.sort_values().plot(kind='barh', color='salmon')
            plt.title('Missing Values per Column')
            plt.xlabel('Count')
            plt.tight_layout()
            plt.savefig(os.path.join(self.output_dir, 'missing_values.png'))
            plt.close()
            logging.info("Missing values plot saved.")
        else:
            logging.info("No missing values to plot.")

    def plot_histograms(self):
        numerical_cols = self.df.select_dtypes(include=['number']).columns
        if len(numerical_cols) > 0:
            self.df[numerical_cols].hist(figsize=(15, 10), bins=20, color='skyblue', edgecolor='black')
            plt.suptitle('Histograms of Numerical Features', fontsize=16)
            plt.tight_layout()
            plt.savefig(os.path.join(self.output_dir, 'histograms.png'))
            plt.close()
            logging.info("Histograms saved.")

    def plot_boxplots(self):
        numerical_cols = self.df.select_dtypes(include=['number']).columns
        if len(numerical_cols) > 0:
            plt.figure(figsize=(15, 8))
            sns.boxplot(data=self.df[numerical_cols], orient='h', palette='Set2')
            plt.title('Boxplots of Numerical Features')
            plt.tight_layout()
            plt.savefig(os.path.join(self.output_dir, 'boxplots.png'))
            plt.close()
            logging.info("Boxplots saved.")

    def plot_correlation_heatmap(self):
        numerical_cols = self.df.select_dtypes(include=['number']).columns
        if len(numerical_cols) > 1:
            plt.figure(figsize=(12, 8))
            corr = self.df[numerical_cols].corr()
            sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
            plt.title('Correlation Heatmap')
            plt.tight_layout()
            plt.savefig(os.path.join(self.output_dir, 'correlation_heatmap.png'))
            plt.close()
            logging.info("Correlation heatmap saved.")
