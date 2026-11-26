# HƯỚNG DẪN ÁNH XẠ SỐ LIỆU TỪ NOTEBOOK TỔNG HỢP VÀO BÀI TẬP VỀ NHÀ

1. **BT1 (Đề xuất & Bước 4 Thu thập/Khám phá):**
   - `RAW_PRE_SPLIT/table_1_1_raw_pre_split_inventory.csv`, `table_1_3_waterfall_filter_summary.csv`, `full_summary.json`
   - `RAW18_SPLIT/table_2_1_ban_tho_18_split_inventory.csv`, `dataset_versions_inventory.csv`
2. **BT2 (Đo lường & Giám sát DAMA 6 chiều):**
   - `DAMA/table_4_1_dama_six_dimensions_overall.csv`, `table_4_2_dama_quarters_comparison.csv`
   - `IMPUTE_BENCHMARK/table_3_1_impute_mae_comparison.csv` (Mask-and-Recover 20 repeats)
3. **BT3 (Thuyết minh Ver 1 - Chương 5 & Chương 6):**
   - `DAMA/*`, `TASK03_NO_DEST/*`, `TASK03_WITH_DEST/*`, `BENCHMARK_3_VERSIONS/*`
   - Xác nhận: `base22` & `prep27` có 92,681,850 dòng sạch (non_cargo NaN = 0).
4. **BT4 & BT5 (Kịch bản triển khai & Benchmark đối sánh):**
   - `BENCHMARK_DS317_04_RAW_CC/table_6a_1_metrics_comparison.csv`
   - `BENCHMARK_3_VERSIONS/benchmark_results_all_versions.csv` & `benchmark_by_horizon.csv`