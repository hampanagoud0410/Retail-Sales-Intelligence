def build_where_clause(state="All", category="All", year="All"):
    conditions = []

    if state != "All":
        conditions.append(f"s.state = '{state}'")

    if category != "All":
        conditions.append(f"c.category_name = '{category}'")

    if year != "All":
        conditions.append(f"strftime('%Y', o.order_date) = '{year}'")

    if conditions:
        return "WHERE " + " AND ".join(conditions)

    return ""
