from pathlib import Path
Path('outputs').mkdir(exist_ok=True)

#import src.url_scraper
#import src.product_scraper
import src.ai_data_extractor  # pyright: ignore[reportUnusedImport]
